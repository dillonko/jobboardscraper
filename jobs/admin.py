from django.contrib import admin

from jobs.models import Board, Job


class BoardAdmin(admin.ModelAdmin):
    list_display = ('title',)


class JobAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Board, BoardAdmin)
admin.site.register(Job, JobAdmin)
