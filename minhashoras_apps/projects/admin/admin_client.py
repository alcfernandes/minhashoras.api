from minhashoras_apps.core.admin import BaseAdmin


class ClientAdmin(BaseAdmin):
    list_display = ['id', 'name', 'email', 'account', 'is_active']
    raw_id_fields = [
        'account',
    ]
    search_fields = [
        'name',
        'account__owner__email',
        'account__id',
    ]
