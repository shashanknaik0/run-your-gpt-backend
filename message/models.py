from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.ForeignKey(to=User,on_delete=models.CASCADE)
    userInput = models.CharField(max_length=255)
    response = models.CharField(max_length=255,null=False)
    createdAt = models.DateTimeField(auto_now_add=True)