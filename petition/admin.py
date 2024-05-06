from .models import Monitoring, Observation, Other, TaskPredeterminate
from django.contrib import admin


class monitoringAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Monitoring model.
    """

    list_display = (
        "id",
        "fullName",
        "petitionDate",
        "state",
        "getUser",
        "getPetitionType",
    )
    list_filter = ("state", "petitionDate")
    search_fields = ("fullName", "email")


admin.site.register(Monitoring, monitoringAdmin)


class otherAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Other model.
    """

    list_display = (
        "id",
        "fullName",
        "petitionDate",
        "state",
        "getUser",
        "getPetitionType",
    )
    list_filter = ("state", "petitionDate")
    search_fields = ("fullName", "email")


admin.site.register(Other, otherAdmin)


class ObservationAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Observation model.
    """

    list_display = ("id", "description", "date", "time", "author", "petition")
    list_filter = ("date",)
    search_fields = ("description", "author")


admin.site.register(Observation, ObservationAdmin)


class TaskPredeterminateAdmin(admin.ModelAdmin):
    """
    Admin configuration for the TaskPrederminate.
    """

    list_display = ("description",)
    search_fields = ("description", "admin")


admin.site.register(TaskPredeterminate, TaskPredeterminateAdmin)
