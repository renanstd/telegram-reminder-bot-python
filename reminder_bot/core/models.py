import uuid
from django.db import models


class Reminder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    message = models.CharField(max_length=255)
    date_hour = models.DateTimeField()
    sent = models.BooleanField(default=False)
    user_id = models.CharField(max_length=255)

    def __str__(self):
        return self.user_id
