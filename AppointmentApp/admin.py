from django.contrib import admin
from AppointmentApp.models import appointment
@admin.register(appointment)
class AppointmentAdminPersonnaliser(admin.ModelAdmin):
    list_display=("reason","status","appointment_date")
    list_filter=("reason","status")