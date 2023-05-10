from django.contrib import admin
from django.utils.translation import gettext as _


class ArchivableAdmin(admin.ModelAdmin):
    actions = ['archive_objects']

    def archive_objects(self, request, queryset):
        for obj in queryset:
            obj.archive()

    archive_objects.short_description = _('Archive selected objects')
