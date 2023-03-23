from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    last_activity = models.DateTimeField(
        default=timezone.now, verbose_name=_("last activity")
    )

    class Meta:
        verbose_name = _("Custom user")
        verbose_name_plural = _("Custom users")

    def __str__(self):
        return self.username
