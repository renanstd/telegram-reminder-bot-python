import datetime
import time
import pytz

import schedule
from telegram import Bot
from telegram.error import Unauthorized

from database import init_database
from models import Reminder
from settings import BOT_TOKEN


TIMEZONE = pytz.timezone("America/Sao_Paulo")


def check_reminders():
    # Inicializa db e bot
    init_database()
    bot = Bot(token=BOT_TOKEN)

    # Busca lembretes que deverão ser enviados
    reminders = Reminder.select().where(
        Reminder.datetime <= datetime.datetime.now(TIMEZONE),
        Reminder.done == False,
    )

    # Envia as mensagens via telegram
    for reminder in reminders:
        try:
            bot.send_message(reminder.chat_id, reminder.reminder)
            reminder.done = True
            reminder.save()
        except Unauthorized:
            # Caso um usuário bloqueie o bot, uma exception é lançada
            continue


schedule.every(5).minutes.do(check_reminders)

while True:
    schedule.run_pending()
    time.sleep(1)
