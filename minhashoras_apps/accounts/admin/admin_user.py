from django.utils import timezone
from django.utils.html import format_html

from minhashoras_apps.core.admin import ArchivableAdmin


class UserAdmin(ArchivableAdmin):
    list_display = ['email', 'name', 'is_staff', 'archived_status']
    list_filter = ('is_active',)

    def delete_model(self, request, obj):
        obj.archived_at = timezone.now()
        obj.is_active = False
        obj.save()

    def archived_status(self, obj):
        if obj.archived_at:
            return format_html(
                '<span style="color: red;">&#x2713;</span>'
            )  # red check mark
        else:
            return format_html(
                '<span style="color: green;">&#x2717;</span>'
            )  # green cross mark

    archived_status.short_description = 'Archived Status'
