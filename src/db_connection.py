from playhouse.db_url import connect
from settings import DATABASE_URL


db = connect(DATABASE_URL)
