from minhashoras_apps.core.admin import BaseAdmin


class ProjectAdmin(BaseAdmin):
    list_display = ['id', 'name', 'is_active']
