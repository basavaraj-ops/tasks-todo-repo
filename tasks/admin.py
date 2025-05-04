from django.contrib import admin
from .models import Task

# Register your models here.
# Customizing the admin interface for Task model
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'date')  # Fields to display in list view
    list_filter = ('completed', 'date')  # Filters to add in the admin interface
    search_fields = ('title', 'description')  # Searchable fields
    
    
admin.site.register(Task,TaskAdmin)


