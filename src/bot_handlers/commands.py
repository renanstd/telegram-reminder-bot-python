from telegram import Update
from telegram.ext import CallbackContext
import datetime
from models import Reminder


def remind_me_in_10(update: Update, _: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    Reminder.create(
        datetime=datetime.datetime.now(),  # TODO: Alterar aqui
        reminder='10 minutos já se passaram!',
        chat_id=chat_id,
    )
    message = "Ok, te chamo de volta daqui 10 minutos!"
    update.message.reply_text(message)


def remind_me_in_30(update: Update, _: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    Reminder.create(
        datetime=datetime.datetime.now(),  # TODO: Alterar aqui
        reminder='30 minutos já se passaram!',
        chat_id=chat_id,
    )
    message = "Ok, te chamo de volta daqui 30 minutos!"
    update.message.reply_text(message)
