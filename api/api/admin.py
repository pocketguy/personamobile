from django.contrib import admin

from .models import Factory, File, Post, Project


class FileAdmin(admin.ModelAdmin):
    ordering = ["created_at"]
    search_fields = ["description"]


class FactoryAdmin(admin.ModelAdmin):
    autocomplete_fields = ["cover"]


class ProjectAdmin(admin.ModelAdmin):
    autocomplete_fields = ["cover"]


class PostAdmin(admin.ModelAdmin):
    autocomplete_fields = ["cover"]


admin.site.register(File, FileAdmin)
admin.site.register(Factory, FactoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Post, PostAdmin)
