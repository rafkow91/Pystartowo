from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(User):
    discord_login = models.CharField(_('Login z Diskord\'a DoKodu.it'), max_length=255, blank=True)
    bio = models.TextField(
        _('O mnie'), blank=True
    )

    def get_absolute_url(self):
        return reverse(
            'users:detail', kwargs={'username': self.username}
        )
