import uuid
import peewee


database_proxy = peewee.DatabaseProxy()


class Reminder(peewee.Model):
    id = peewee.UUIDField(primary_key=True, default=uuid.uuid4)
    chat_id = peewee.CharField(max_length=255)
    datetime = peewee.DateTimeField()
    reminder = peewee.CharField(max_length=255)
    done = peewee.BooleanField(default=False)

    class Meta:
        database = database_proxy
