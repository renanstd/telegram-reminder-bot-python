from django.contrib import admin
from core import models


@admin.register(models.Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_filter = ['sent']
    list_display = ['user_id', 'message', 'date_hour', 'sent']
