from django.db import models

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    task = models.CharField(max_length=200)
    status = models.CharField(
        max_length=12,
        choices=STATUS_CHOICES,
        default='not_started',
    )
    
    def __str__(self):
        return self.task
