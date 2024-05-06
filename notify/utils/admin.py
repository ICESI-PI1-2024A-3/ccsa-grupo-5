from django.contrib import admin
from notify.utils.models import AbstractNotification
from notify.models import Notification  # Asegúrate de importar tu modelo Notification desde su ubicación actual

class AbstractNotifyAdmin(admin.ModelAdmin):
    
    raw_id_fields = ('destiny',)
    list_display = ('destiny', 'actor', 'verb', 'read', 'public')
    list_filter = ('levels', 'read')  # Corregido 'level' a 'levels' según el modelo
    search_fields = ('destiny__username', 'actor__username', 'verb')  # Si es necesario, agrega campos de búsqueda
    date_hierarchy = 'timestamp'  # Si es necesario, agrega jerarquía de fechas
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('actor')
