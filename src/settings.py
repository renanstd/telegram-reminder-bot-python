from decouple import config


DATABASE_URL = config(
    "DATABASE_URL", default="postgresql://postgres:admin@db/reminders"
)
BOT_TOKEN = config("BOT_TOKEN")
ENVIRONMENT = config("ENVIRONMENT", default="prod")
PORT = config("PORT", default="8443", cast=int)
APP_URL = config("APP_URL", default="")
