from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext as _


class ArchivableAdmin(admin.ModelAdmin):
    actions = ['archive_objects']

    def archive_objects(self, request, queryset):
        for obj in queryset:
            obj.archive()

    archive_objects.short_description = _('Archive selected objects')

    def archived_status(self, obj):
        if obj.archived_at:
            return format_html(
                '<span style="color: red;">&#x2713;</span>'
            )  # red check mark
        else:
            return format_html(
                '<span style="color: green;">&#x2717;</span>'
            )  # green cross mark

    archived_status.short_description = _('Archived Status')
