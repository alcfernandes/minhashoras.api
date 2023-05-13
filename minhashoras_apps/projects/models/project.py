from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _

from minhashoras_apps.core.models import AbstractBaseModel


class Project(AbstractBaseModel):
    account = models.ForeignKey(
        'accounts.Account',
        on_delete=models.CASCADE,
        related_name='projects',
        verbose_name=_('account'),
    )

    client = models.ForeignKey(
        'Client',
        on_delete=models.CASCADE,
        related_name='projects',
        verbose_name=_('client'),
    )

    name = models.CharField(
        max_length=100,
        verbose_name=_('name'),
    )

    description = RichTextField(
        blank=True,
        verbose_name=_('description'),
        help_text=_('Description of the project'),
    )

    def __str__(self):
        return f'{self.name} #{self.id}'

    class Meta:
        verbose_name = _('project')
        verbose_name_plural = _('projects')
        unique_together = ('account', 'name')
