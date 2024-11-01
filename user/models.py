"""Django model for user login and sign up functionality"""

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """User profile model extending the built-in User model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)
    travel_preferences = models.CharField(max_length=255, blank=True)
    likes = models.CharField(max_length=255, blank=True)
    is_smoker = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s Profile"