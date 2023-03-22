from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    last_activity = models.DateTimeField(default=timezone.now)
    last_login_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username
