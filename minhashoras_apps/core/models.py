import uuid as uuid

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class ActiveObjectsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(archived_at__isnull=True)


class AbstractBaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name=_('created at')
    )
    updated_at = models.DateTimeField(
        auto_now=True, editable=False, verbose_name=_('updated at')
    )
    archived_at = models.DateTimeField(
        null=True, blank=True, verbose_name=_('archived at')
    )
    is_active = models.BooleanField(default=True, verbose_name=_('is active?'))

    objects = models.Manager()
    active_objects = ActiveObjectsManager()

    class Meta:
        abstract = True

    @classmethod
    def by_id(cls, _id):
        return cls.objects.get(id=_id)

    @classmethod
    def by_uuid(cls, _uuid):
        return cls.objects.get(uuid=_uuid)

    def archive(self):
        self.archived_at = timezone.now()
        self.is_active = False
        self.save()
