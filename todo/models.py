from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)  # Corrected the typo here
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    duedate = models.DateField(blank=True, null=True)
    duetime = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {'Complete' if self.complete else 'Incomplete'}"
