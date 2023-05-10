from minhashoras_apps.core.admin import ArchivableAdmin


class UserAdmin(ArchivableAdmin):
    list_display = ['email', 'name', 'is_staff', 'is_active']
