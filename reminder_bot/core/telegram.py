import os
import django
from django.conf import settings
from telegram.ext import (
    Updater,
    MessageHandler,
    CommandHandler,
    Filters
)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reminder_bot.settings')
django.setup()


from core import models


BOT_TOKEN = settings.BOT_TOKEN
updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher


def handle_message(update, context):
    chat_id = update.effective_chat.id
    message = update.message.text.lower()
    print(chat_id)
    print(message)


def handle_quit(update, context):
    exit(0)


quit_command = CommandHandler('quit', handle_quit)
message_handler = MessageHandler(Filters.text, handle_message)

dispatcher.add_handler(message_handler)
dispatcher.add_handler(quit_command)

if settings.ENVIRONMENT == 'dev':
    updater.start_polling()
else:
    PORT = os.getenv('PORT')
    HEROKU_URL = os.getenv('HEROKU_URL')
    updater.start_webhook(
        listen='localhost',
        port=PORT,
        url_path=BOT_TOKEN
    )
    updater.bot.set_webhook(HEROKU_URL + BOT_TOKEN)

print("Mozão ta on!")
