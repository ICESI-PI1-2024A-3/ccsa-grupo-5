from notify import models as nm

def notifications_context(request):
    if request.user.is_authenticated:
        user = request.user
        notifications = nm.Notification.objects.filter(destiny=user)
    else:
    # El usuario no está autenticado, manejar el caso en consecuencia
        notifications = []

    
    return {'notifications': notifications}
