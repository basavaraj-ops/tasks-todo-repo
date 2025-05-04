from django.db import models



# Task model to represent tasks in the task management system
class Task(models.Model):
    # Task title (short text field)
    title = models.CharField(max_length=200)

    # Task description (long text field, can be left empty)
    description = models.TextField(blank=True, null=True)

    # Completion status of the task
    completed = models.BooleanField(default=False, blank=True, null=True)

    # Date when the task is created or due
    date = models.DateField()

    # String representation of the Task object, will show the title
    def __str__(self):
        return self.title

    

