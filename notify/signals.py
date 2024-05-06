from django.dispatch import Signal

from django.dispatch import Signal

# Define la señal
notify = Signal()

# Emite la señal con los argumentos como un diccionario
notify.send(sender=None, kwargs={
    'level': 'info',
    'destiny': 'user',
    'actor': 'admin',
    'verb': 'create',
    'timestamp': '2000-05-06',
})
