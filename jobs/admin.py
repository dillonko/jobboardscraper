from django.contrib import admin

from jobs.models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Job, JobAdmin)
