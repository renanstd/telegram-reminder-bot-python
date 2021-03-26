from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from database import init_database
from settings import ENVIRONMENT, BOT_TOKEN, PORT, HEROKU_URL
from bot_handlers.commands import (
    remind_me_in_10_minutes,
    remind_me_in_30_minutes,
    remind_me_in_1_hour
)
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
    remind_me_in_10_minutes
))
dispatcher.add_handler(CommandHandler(
    "30m",
    remind_me_in_30_minutes
))
dispatcher.add_handler(CommandHandler(
    "1h",
    remind_me_in_1_hour
))


if ENVIRONMENT == 'dev':
    updater.start_polling()
    updater.idle()
else:
    updater.start_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=BOT_TOKEN,
        webhook_url=HEROKU_URL + BOT_TOKEN
    )
    updater.idle()
