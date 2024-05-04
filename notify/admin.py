from django.contrib import admin
from notify.utils.admin import AbstractNotifyAdmin

# Register your models here.

from .models import Notification

admin.site.register(Notification, AbstractNotifyAdmin)