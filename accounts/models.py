from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(
        _('email address'),
        unique=True,
        blank=False,
        error_messages={
            'unique': _("Bu e-posta adresi ile zaten bir hesap var."),
        },
    )

    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('Kullanıcı')
        verbose_name_plural = _('Kullanıcılar')

    def __str__(self):
        return self.username
