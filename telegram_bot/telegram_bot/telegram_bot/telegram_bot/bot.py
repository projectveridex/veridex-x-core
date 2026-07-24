"""
VERIDEX X
Telegram Bot
"""

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from telegram_bot.config import BOT_TOKEN
from telegram_bot.dashboard import dashboard


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(dashboard())


async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🔍 VERIDEX has started scanning..."
    )


def build_bot():

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(CommandHandler("scan", scan))

    return app
