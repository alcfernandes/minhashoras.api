from minhashoras_apps.core.admin import BaseAdmin


class AccountAdmin(BaseAdmin):
    list_display = ['id', 'name', 'owner', 'is_active']
    search_fields = [
        'name',
        'id',
        'uuid',
        'users__email',
    ]
