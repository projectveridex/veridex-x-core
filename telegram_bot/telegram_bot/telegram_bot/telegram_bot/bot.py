"""
VERIDEX X
Telegram Bot
"""

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from telegram_bot.config import BOT_TOKEN
from telegram_bot.dashboard import dashboard

from core.controller import (
    run_veridex,
    get_last_scan,
    get_approval_queue
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(dashboard())


async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text("🔍 VERIDEX is scanning...")

    run_veridex()

    jobs = get_last_scan()

    await update.message.reply_text(
        f"""
🔥 VERIDEX REPORT

Live Opportunities Found: {len(jobs)}

Type /jobs to view them.
"""
    )


async def jobs(update: Update, context: ContextTypes.DEFAULT_TYPE):

    opportunities = get_last_scan()

    if not opportunities:

        await update.message.reply_text(
            "❌ No scan results available.\nRun /scan first."
        )
        return

    message = "📋 Latest Opportunities\n\n"

    for i, job in enumerate(opportunities[:10], start=1):
        message += f"{i}. {job.title} ({job.source})\n"

    if len(opportunities) > 10:
        message += f"\n...and {len(opportunities) - 10} more."

    message += "\n\nUse /approve <number>"

    await update.message.reply_text(message)


async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:

        await update.message.reply_text(
            "Usage:\n/approve 1"
        )
        return

    try:

        index = int(context.args[0]) - 1

    except ValueError:

        await update.message.reply_text(
            "Job number must be a number."
        )
        return

    queue = get_approval_queue()

    approved = queue.approve(index)

    if approved is None:

        await update.message.reply_text(
            "❌ Invalid job number."
        )
        return

    await update.message.reply_text(
        f"✅ Approved:\n{approved['opportunity'].title}"
    )


def build_bot():

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("scan", scan))
    app.add_handler(CommandHandler("jobs", jobs))
    app.add_handler(CommandHandler("approve", approve))

    return app
