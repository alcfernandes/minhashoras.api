from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from minhashoras_apps.core.models import AbstractBaseModel


class Account(AbstractBaseModel):
    name = models.CharField(
        max_length=250,
        verbose_name=_('name'),
    )

    def __str__(self):
        return self.name

    @property
    def owner(self):
        return self.users.filter(is_owner=True).first()

    def set_owner(self, new_owner, force=False):
        if new_owner.account != self:
            raise ValidationError(
                _('The new owner must belong to the same account.')
            )

        current_owner = self.owner

        if current_owner:
            if force:
                current_owner.is_owner = False
                current_owner.save()
            else:
                raise ValidationError(
                    _(
                        f'The account already has an owner: {current_owner.email}'
                    )
                )

        new_owner.is_owner = True
        new_owner.save()

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')
