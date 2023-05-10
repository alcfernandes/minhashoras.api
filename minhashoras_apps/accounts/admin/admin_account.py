from django.utils import timezone

from minhashoras_apps.core.admin import ArchivableAdmin


class AccountAdmin(ArchivableAdmin):
    list_display = ['id', 'owner', 'archived_status']
    # list_filter = ('is_active',)
