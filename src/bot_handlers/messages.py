import re
import datetime
import pytz

from telegram import Update
from telegram.ext import CallbackContext

from models import Reminder


TIMEZONE = pytz.timezone("America/Sao_Paulo")


def handle_message(update: Update, _: CallbackContext) -> None:
    chat_id = update.effective_chat.id
    message = update.message.text

    regex_date = re.compile("\d{2}\/\d{2}\/\d{4}")
    regex_tomorrow = re.compile("amanhã|amanha")
    regex_today = re.compile("hoje")
    regex_hour = re.compile("\d{1,2}[h|:]\d{2}")
    regex_reminder = re.compile("^[^,]*")

    date = regex_date.findall(message)
    date_tomorrow = regex_tomorrow.findall(message)
    date_today = regex_today.findall(message)
    hour = regex_hour.findall(message)
    reminder = regex_reminder.findall(message)

    if date_today:
        today = datetime.datetime.now(TIMEZONE)
        datetime_obj = datetime.datetime.strptime(
            today.strftime("%d/%m/%Y") + hour[0], "%d/%m/%Y%H:%M"
        )
    elif date_tomorrow:
        today = datetime.datetime.now(TIMEZONE)
        tomorrow = today + datetime.timedelta(days=1)
        datetime_obj = datetime.datetime.strptime(
            tomorrow.strftime("%d/%m/%Y") + hour[0], "%d/%m/%Y%H:%M"
        )
    else:
        datetime_obj = datetime.datetime.strptime(
            date[0] + hour[0], "%d/%m/%Y%H:%M"
        )

    # Add timezone info
    datetime_obj = TIMEZONE.localize(datetime_obj)

    Reminder.create(
        datetime=datetime_obj, reminder=reminder[0], chat_id=chat_id
    )

    answer = "Ok, te lembrarei de {}, no dia {} às {}.".format(
        reminder[0],
        datetime_obj.strftime("%d/%m/%Y"),
        datetime_obj.strftime("%H:%M"),
    )
    update.message.reply_text(answer)
