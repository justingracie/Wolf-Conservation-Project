from django.db import models
from django.forms import CharField

# Create your models here.
class Video(models.Model):
    # video=models.FileField(upload_to="video/%y", default='no video')
    link=models.CharField(max_length=400, default='no link')
    title=models.CharField(max_length=125, default='no title')

    def __str__(self):
        return self.title


class Pack(models.Model):
    name = models.CharField(max_length=125, default='unassigned')
    founded = models.CharField(max_length=50, default=0)
    adults = models.CharField(max_length=25, default=0)
    pups = models.CharField(max_length=25, default=0)
    total = models.CharField(max_length=25, default=0)
    history = models.CharField(max_length=1200, default='No info available')
    img = models.CharField(max_length=500, default='no image')

    def __str__(self):
        return self.name
