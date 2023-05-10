from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class ArchivableAdmin(admin.ModelAdmin):
    actions = ['archive_objects']
    list_filter = ('is_active',)

    def archive_objects(self, request, queryset):
        for obj in queryset:
            obj.archive()

    archive_objects.short_description = _('Archive selected objects')
