from telegram_bot.bot import build_bot


def main():

    app = build_bot()

    app.run_polling()


if __name__ == "__main__":

    main()
