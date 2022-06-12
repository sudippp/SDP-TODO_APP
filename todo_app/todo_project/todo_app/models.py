from django.db import models

# Create your models here.

class TodoModel(models.Model):
    task = models.CharField(max_length=50)
    details = models.TextField(max_length=50)
    priority = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.CharField(max_length=70)