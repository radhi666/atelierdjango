from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, Doctor, Patient, Specialty
from django.contrib.auth.admin import UserAdmin
admin.site.register(User, UserAdmin)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Specialty)
