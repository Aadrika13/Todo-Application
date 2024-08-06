from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.TextField()
    created_at = models.DateField()

    is_completed = models.BooleanField(default = False)

    def __str__(self):
        return self.task

class Profile(models.Model):
    title = models.CharField(max_length=30)
    profile = models.ImageField(upload_to='profile/')