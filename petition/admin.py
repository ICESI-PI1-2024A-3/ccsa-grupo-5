from .models import Monitoring, Observation, Other
from django.contrib import admin


class monitoringAdmin(admin.ModelAdmin):
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
    list_display = ("id", "description", "date", "time", "author", "petition")
    list_filter = ("date",)
    search_fields = ("description", "author")


admin.site.register(Observation, ObservationAdmin)
