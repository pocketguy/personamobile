from django.contrib import admin

from .models import Factory


class FactoryAdmin(admin.ModelAdmin):
    pass
    # prepopulated_fields = {"slug": ("name",)}


admin.site.register(Factory, FactoryAdmin)

# Register your models here.
