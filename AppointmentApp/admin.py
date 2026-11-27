from django.contrib import admin

# AppointmentApp/admin.py
from django.contrib import admin
from .models import Appointment
@admin.register(Appointment)
class AppointmentAdminPerso(admin.ModelAdmin):
    list_display = ('id', 'reason', 'status','duration_minutes', 'appointment_date','doctor', 'patient',)
    list_filter = ('status', 'appointment_date')
    list_editable = ('status',) 
    search_fields = ('duration_minutes',
'doctor__username',)
    list_per_page = 2 
    ordering = ('appointment_date',)