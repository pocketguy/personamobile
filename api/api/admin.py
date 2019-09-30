from django.contrib import admin

from .models import Factory, File


class FileAdmin(admin.ModelAdmin):
    ordering = ["created_at"]
    search_fields = ["description"]


class FactoryAdmin(admin.ModelAdmin):
    autocomplete_fields = ["cover"]


admin.site.register(Factory, FactoryAdmin)
admin.site.register(File, FileAdmin)
