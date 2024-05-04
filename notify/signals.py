from django.dispatch import Signal

notify = Signal(providing_args=[
    'level',
    'destiny',
    'actor',
    'verb',
    'timestamp',
                    ])