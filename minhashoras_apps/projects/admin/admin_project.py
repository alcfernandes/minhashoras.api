from minhashoras_apps.core.admin import BaseAdmin


class ProjectAdmin(BaseAdmin):
    list_display = ['id', 'name', 'client', 'account', 'is_active']
    raw_id_fields = ['account', 'client']
    search_fields = [
        'name',
        'client__name',
        'account__owner__email',
        'account__id',
        'client__id',
    ]
