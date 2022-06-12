
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User
# Create your models here.
class Video(models.Model):
    video=models.FileField(upload_to="video/", default='no video')
    title=models.CharField(max_length=125, default='no title')

    def __str__(self):
        return self.title


class Pack(models.Model):
    name = models.CharField(max_length=125, default='unassigned')
    founded = models.CharField(max_length=50, default=0)
    adults = models.CharField(max_length=25, default=0)
    pups = models.CharField(max_length=25, default=0)
    total = models.CharField(max_length=25, default=0)
    history = models.TextField(max_length=1200, default='No info available')
    img = models.CharField(max_length=500, default='no image')

    def __str__(self):
        return self.name

class Story(models.Model):
    name = models.CharField(max_length=125)
    title = models.CharField(max_length=125)
    story = models.TextField(max_length=2000, default='noting yet')
    story_Img = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name