from django.apps import AppConfig


class AccountappConfig(AppConfig):
    name = 'AccountApp'
AUTH_USER_MODEL = 'AccountApp.User'