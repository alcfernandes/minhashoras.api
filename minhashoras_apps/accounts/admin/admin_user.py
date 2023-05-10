from django.utils import timezone

from minhashoras_apps.core.admin import ArchivableAdmin


class UserAdmin(ArchivableAdmin):
    list_display = ['email', 'name', 'is_staff', 'archived_status']
    list_filter = ('is_active',)
