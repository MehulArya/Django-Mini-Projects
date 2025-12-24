from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Note(models.Model):
    text = models.CharField(max_length=30)
    body = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
