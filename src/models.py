import peewee


database_proxy = peewee.DatabaseProxy()


class Reminder(peewee.Model):
    id = peewee.UUIDField(primary_key=True)
    datetime = peewee.DateTimeField()
    reminder = peewee.CharField(max_length=255)
    done = peewee.BooleanField(default=False)

    class Meta:
        database = database_proxy
