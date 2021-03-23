from telegram import Update
from telegram.ext import CallbackContext
from models import Reminder


def handle_message(update: Update, _: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    message = update.message.text
    update.message.reply_text(message)
