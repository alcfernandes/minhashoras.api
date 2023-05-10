from minhashoras_apps.core.admin import ArchivableAdmin


class AccountAdmin(ArchivableAdmin):
    list_display = ['id', 'owner', 'is_active']
