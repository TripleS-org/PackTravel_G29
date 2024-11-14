"""Django app for user login and sign up functionality"""
from django.apps import AppConfig


class UserConfig(AppConfig):
    """Configuration for the 'user' Django app, handling user authentication features."""
    
    default_auto_field = "django.db.models.BigAutoField"
    name = "user"
