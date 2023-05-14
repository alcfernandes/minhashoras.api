from minhashoras_apps.core.admin import BaseAdmin


class UserAdmin(BaseAdmin):
    list_display = [
        'email',
        'name',
        'is_staff',
        'account',
        'is_owner',
        'is_active',
    ]
    search_fields = [
        'email',
        'name',
        'uuid',
        'account__name',
        'account__id',
        'account__uuid',
    ]
    raw_id_fields = [
        'account',
    ]
    list_filter = ['is_staff', 'is_owner', 'account']
