from django.apps import AppConfig


class AppointmentappConfig(AppConfig):
    name = 'AppointmentApp'
    AUTH_USER_MODEL = 'AccountApp.User'
