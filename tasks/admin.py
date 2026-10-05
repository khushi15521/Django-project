from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'priority', 'due_date', 'completed')
    list_filter = ('completed', 'priority', 'category', 'due_date')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
