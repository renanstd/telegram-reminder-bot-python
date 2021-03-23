from decouple import config


DATABASE_URL = config('DATABASE_URL')
BOT_TOKEN = config('BOT_TOKEN')
ENVIRONMENT = config('ENVIRONMENT', default='prod')
PORT = config('PORT', default="8443", cast=int)
HEROKU_URL = config('HEROKU_URL')
