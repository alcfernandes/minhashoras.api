from django.db import models
from django.utils.translation import gettext_lazy as _

from minhashoras_apps.core.models import AbstractBaseModel


class Account(AbstractBaseModel):
    owner = models.OneToOneField(
        'User',
        on_delete=models.CASCADE,
        related_name='owned_account',
        verbose_name=_('owner'),
    )

    def __str__(self):
        return self.owner.email

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')
