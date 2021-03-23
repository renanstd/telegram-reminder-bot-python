from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from database import init_database
from settings import ENVIRONMENT, BOT_TOKEN, PORT, HEROKU_URL
from bot_handlers.commands import remind_me_in_10, remind_me_in_30
from bot_handlers.messages import handle_message


init_database()
updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher =updater.dispatcher

dispatcher.add_handler(MessageHandler(
    Filters.text & ~Filters.command,
    handle_message
))
dispatcher.add_handler(CommandHandler(
    "10m",
    remind_me_in_10
))
dispatcher.add_handler(CommandHandler(
    "30m",
    remind_me_in_30
))


if ENVIRONMENT == 'dev':
    updater.start_polling()
    updater.idle()
else:
    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    print(PORT)
    updater.start_webhook(
        listen='0.0.0.0',
        port=PORT,
        url_path=BOT_TOKEN,
    )
    updater.bot.set_webhook(HEROKU_URL + BOT_TOKEN)
