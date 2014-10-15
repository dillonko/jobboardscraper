from django.contrib import admin

from .models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Organization, OrganizationAdmin)
