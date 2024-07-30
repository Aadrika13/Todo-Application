from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.TextField()
    created_at = models.DateField()

    is_completed = models.BooleanField(default = False)

class Profile(models.Model):
    title = models.CharField(max_length=30)
    profile = models.ImageField(upload_to='profile/')