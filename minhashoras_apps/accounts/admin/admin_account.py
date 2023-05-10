from minhashoras_apps.core.admin import BaseAdmin


class AccountAdmin(BaseAdmin):
    list_display = ['id', 'owner', 'is_active']
