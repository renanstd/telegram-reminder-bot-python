from telegram import Update
from telegram.ext import CallbackContext
import datetime
from models import Reminder


def formatted_time(time):
    return time.strftime("%H:%M")


def welcome(update: Update, _: CallbackContext) -> None:
    welcome_message = (
        "Seja bem vindo(a) ao Reminder Bot!\n\n"
        "Para lembretes rápidos, como 'Me chame em 10 min', utilize os "
        "commands.\n\n"
        "Para lembretes mais elaborados, digite o que deseja que eu te "
        "lembre, informando a data e hora nos formatos DD/MM/YYYY e HH:MM "
        "respectivamente.\n\nEu também consigo reconhecer palavras chave "
        "como 'hoje' e 'amanhã'.\nExemplos:\n\n"
        "- 'Beber água, amanhã as 08:00'\n"
        "- 'Estudar, hoje as 19:00'\n"
        "- 'Agendar vacina, dia 22/08/2021 08:00"
    )
    update.message.reply_text(welcome_message)


def remind_me_in_10_minutes(update: Update, _: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    reminder_time = datetime.datetime.now() + datetime.timedelta(minutes=10)
    Reminder.create(
        datetime=reminder_time,
        reminder="10 minutos já se passaram!",
        chat_id=chat_id,
    )
    message = "Ok, te chamo de volta as {}".format(
        formatted_time(reminder_time)
    )
    update.message.reply_text(message)


def remind_me_in_30_minutes(update: Update, _: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    reminder_time = datetime.datetime.now() + datetime.timedelta(minutes=30)
    Reminder.create(
        datetime=reminder_time,
        reminder="30 minutos já se passaram!",
        chat_id=chat_id,
    )
    message = "Ok, te chamo de volta as {}".format(
        formatted_time(reminder_time)
    )
    update.message.reply_text(message)


def remind_me_in_1_hour(update: Update, _: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    reminder_time = datetime.datetime.now() + datetime.timedelta(hours=1)
    Reminder.create(
        datetime=reminder_time,
        reminder="1 hora já se passou!",
        chat_id=chat_id,
    )
    message = "Ok, te chamo de volta as {}".format(
        formatted_time(reminder_time)
    )
    update.message.reply_text(message)


def remind_me_in_1_day(update: Update, _: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    reminder_time = datetime.datetime.now() + datetime.timedelta(days=1)
    Reminder.create(
        datetime=reminder_time,
        reminder="1 dia já se passou!",
        chat_id=chat_id,
    )
    message = "Ok, te chamo de volta amanhã as {}".format(
        formatted_time(reminder_time)
    )
    update.message.reply_text(message)
