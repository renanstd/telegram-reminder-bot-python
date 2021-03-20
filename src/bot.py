from telegram import Update
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters, CallbackContext
from database import init_database
from settings import ENVIRONMENT, BOT_TOKEN, PORT, HEROKU_URL


init_database()
updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher =updater.dispatcher


def handle_message(update: Update, context: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    message = update.message.text
    context.bot.send_message(chat_id=chat_id, text=message)


message_handler = MessageHandler(Filters.text, handle_message)

dispatcher.add_handler(message_handler)


if ENVIRONMENT == 'dev':
    updater.start_polling()
    updater.idle()
else:
    updater.start_webhook(
        listen='0.0.0.0',
        port=PORT,
        url_path=BOT_TOKEN,
    )
    updater.bot.set_webhook(HEROKU_URL + BOT_TOKEN)
