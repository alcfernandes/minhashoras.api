from minhashoras_apps.core.admin import BaseAdmin


class ProjectAdmin(BaseAdmin):
    list_display = ['id', 'name', 'client', 'account', 'is_active']
    raw_id_fields = ['account', 'client']
    search_fields = [
        'name',
        'uuid',
        'client__name',
        'client__uuid',
        'account__name',
        'account__id',
        'account__uuid',
    ]
    list_filter = [
        'account',
    ]
