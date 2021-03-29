import re
from telegram import Update
from telegram.ext import CallbackContext
from models import Reminder


def handle_message(update: Update, _: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    message = update.message.text

    regex_date = re.compile('\d{2}\/\d{2}\/\d{4}')
    regex_tomorrow = re.compile('amanhã|amanha')
    regex_today = re.compile('hoje')    
    
    date = regex_date.findall(message)
    tomorrow = regex_tomorrow.findall(message)
    today = regex_today.findall(message)

    # message = "Ok, te lembrarei de {}, no dia {} as {}.".format()
    update.message.reply_text(date + tomorrow + today)
