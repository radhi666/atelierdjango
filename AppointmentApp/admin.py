from django.contrib import admin

# AppointmentApp/admin.py
from django.contrib import admin
from .models import Appointment
admin.site.register(Appointment)