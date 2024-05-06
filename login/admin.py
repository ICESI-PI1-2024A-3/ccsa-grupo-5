from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    """
    Admin configuration for the User model.
    """
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "date_joined",
        "getGroup",
    )
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")


admin.site.register(User, UserAdmin)
