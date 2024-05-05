from django.db import models
from notify.utils.models import AbstractNotification

# Create your models here.

class Notification(AbstractNotification):
    class Meta(AbstractNotification.Meta):
        abstract = False