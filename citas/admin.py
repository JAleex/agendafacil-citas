from django.contrib import admin

from .models import Cita


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ["cliente", "servicio", "fecha", "hora"]
    list_filter = ["servicio", "fecha"]
