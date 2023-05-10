from minhashoras_apps.core.admin import BaseAdmin


class UserAdmin(BaseAdmin):
    list_display = ['email', 'name', 'is_staff', 'is_active']
