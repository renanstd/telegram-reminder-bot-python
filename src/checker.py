import datetime
from database import init_database
from models import Reminder
from telegram import Bot
from settings import BOT_TOKEN


TIMEZONE = datetime.timezone(datetime.timedelta(hours=-3))


# Inicializa db e bot
init_database()
bot = Bot(token=BOT_TOKEN)

# Busca lembretes que deverão ser enviados
reminders = Reminder.select().where(
    Reminder.datetime <= datetime.datetime.now(TIMEZONE),
    Reminder.done == False
)

# Envia as mensagens via telegram
for reminder in reminders:
    bot.send_message(reminder.chat_id, reminder.reminder)
    reminder.done = True
    reminder.save()
