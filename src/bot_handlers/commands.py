from telegram import Update
from telegram.ext import CallbackContext
import datetime
from models import Reminder


def remind_me_in_10_minutes(update: Update, _: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    reminder_time = datetime.datetime.now() + datetime.timedelta(minutes=10)
    Reminder.create(
        datetime=reminder_time,
        reminder='10 minutos já se passaram!',
        chat_id=chat_id,
    )
    message = "Ok, te chamo de volta daqui 10 minutos."
    update.message.reply_text(message)


def remind_me_in_30_minutes(update: Update, _: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    reminder_time = datetime.datetime.now() + datetime.timedelta(minutes=30)
    Reminder.create(
        datetime=reminder_time,
        reminder='30 minutos já se passaram!',
        chat_id=chat_id,
    )
    message = "Ok, te chamo de volta daqui 30 minutos."
    update.message.reply_text(message)


def remind_me_in_1_hour(update: Update, _: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    reminder_time = datetime.datetime.now() + datetime.timedelta(hours=1)
    Reminder.create(
        datetime=reminder_time,
        reminder='1 hora já se passou!',
        chat_id=chat_id,
    )
    message = "Ok, te chamo de volta daqui 1 hora."
    update.message.reply_text(message)


def remind_me_in_1_day(update: Update, _: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    reminder_time = datetime.datetime.now() + datetime.timedelta(days=1)
    Reminder.create(
        datetime=reminder_time,
        reminder='1 dia já se passou!',
        chat_id=chat_id,
    )
    message = "Ok, te chamo de volta daqui 1 dia."
    update.message.reply_text(message)
