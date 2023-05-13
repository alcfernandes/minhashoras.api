from minhashoras_apps.core.admin import BaseAdmin


class ClientAdmin(BaseAdmin):
    list_display = ['id', 'name', 'email', 'is_active']
