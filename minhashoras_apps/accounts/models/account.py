from django.db import models

from minhashoras_apps.core.models import AbstractBaseModel


class Account(AbstractBaseModel):
    owner = models.OneToOneField(
        'User', on_delete=models.CASCADE, related_name='owned_account'
    )

    def __str__(self):
        return self.owner.email
