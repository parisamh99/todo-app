from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title','created_date','completed']
    list_filter = ['title','created_date','completed']

admin.site.register(Task,TaskAdmin)
