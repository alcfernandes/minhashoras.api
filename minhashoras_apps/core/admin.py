from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class BaseAdmin(admin.ModelAdmin):
    actions = ['archive_objects']
    list_filter = ('is_active',)
    readonly_fields = ('id', 'created_at', 'updated_at', 'is_active', 'uuid')

    def archive_objects(self, request, queryset):
        for obj in queryset:
            obj.archive()

    archive_objects.short_description = _('Archive selected objects')
