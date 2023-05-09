from django.contrib import admin


class ArchivableAdmin(admin.ModelAdmin):
    actions = ['archive_objects']

    def archive_objects(self, request, queryset):
        for obj in queryset:
            obj.archive()

    archive_objects.short_description = 'Arquivar objetos selecionados'
