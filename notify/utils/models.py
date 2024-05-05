from django.db import models
from django.contrib.contenttypes.models import ContentType 
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import Group
from django.db.models.query import QuerySet
from notify.signals import notify
from django.utils import timezone
from login.models import User 
from swapper import load_model

class NotificationQuerySet(models.QuerySet):
    def read (self, include_deleted=True):
        """
        Retornar notificaciones leidas
        """
        if include_deleted:
            return self.filter(read=True)
    
    def unread (self, include_deleted=False):
        if include_deleted==True:
            return self.filter(read=False)
    
    def all_as_read (self, destiny):
        qs = self.read(False)
        if destiny:
            qs = qs.filter(destiny)
        return qs.update(read=True)
    
    def all_as_unread (self, destiny=None):
        qs = self.read(True)
        if destiny:
            qs = qs.filter(destiny=destiny)
        return qs.update(read=False) 

class AbstractNotificationManager (models.Manager):
    def get_queryset(self):
        return self.NoticationQuerySet(self.Model, using=self._db)
    

class AbstractNotification(models.Model):
    
    #Dijo que esto era el objetivo de la notificación 
    class levels(models.TextChoices):
        success = 'Success', 'success',
        info = 'Info', 'info',
        wrong = 'Wrong', 'wrong',
    
    levels = models.CharField(choices=levels.choices, max_length=20, default=levels.info)
    
    #Destinatario 
    destinity = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications', blank=True, null=True)
    
    actor_content_type = models.ForeignKey(ContentType, related_name='notify_actor', on_delete=models.CASCADE )
    obj_id_actor = models.PositiveIntegerField()
    actor = GenericForeignKey('actor_content_type', 'obj_id_actor')
    
    verb = models.CharField(max_length=220)
    
    timestamp = models.DateField(default=timezone.now, db_index=True)
    
    read = models.BooleanField(default=False)  
    
    objects = NotificationQuerySet.as_manager()
    public = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    
    class Meta:
        abstract = True

def notify_signals(verb, **kwargs):
    destiny = kwargs.pop('destiny')       
    actor = kwargs.pop('sender') 
    public = bool(kwargs.pop('publico', True))
    timestamp = kwargs.pop('timestamp', timezone.now())
    
    Notify = load_model('notify', 'Notification')
    levels = kwargs.pop('level', Notify.Levels.info)
    
    if isinstance(destiny, Group):
        destinies = destiny.user_set.all()
    elif isinstance(destiny,(QuerySet, list)):
        destinies = destiny
    else:
        destinies = [destiny]
    
    new_notify = []
    for destiny in destinies:
        notification = Notify(
                destiny = destiny,
                actor_content_type=ContentType.objects.get_for_model('actor'),
                object_id_actor = actor.pk,
                verb = str(verb),
                public = public,
                timestamp = timestamp,
                levels = levels
        )
        notification.save()
        new_notify.append(notification)
        return new_notify
            
notify.connect(notify_signals, dispatch_uid='notify.models.Notification')