from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
    type=models.CharField(max_length=20)
    
    
class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=timezone.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
class Sticker(models.Model):
    image = models.ImageField(upload_to='stickers/')
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)