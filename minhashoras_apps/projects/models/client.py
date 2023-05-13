from ckeditor.fields import RichTextField
from django.core.validators import EmailValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from minhashoras_apps.core.models import AbstractBaseModel


class Client(AbstractBaseModel):
    account = models.ForeignKey(
        'accounts.Account',
        on_delete=models.CASCADE,
        related_name='clients',
        verbose_name=_('account'),
    )

    name = models.CharField(
        max_length=100,
        verbose_name=_('name'),
    )

    email = models.EmailField(
        max_length=254,
        validators=[EmailValidator],
        verbose_name=_('email'),
        blank=True,
        null=True,
    )

    notes = RichTextField(
        blank=True,
        verbose_name=_('notes'),
        help_text=_('Notes about the client.'),
    )

    def __str__(self):
        return f'{self.name} #{self.id}'

    class Meta:
        verbose_name = _('client')
        verbose_name_plural = _('clients')
        unique_together = ('account', 'name')
