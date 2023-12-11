from django.db import models

# Create your models here.
from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False

class News(models.Model):
    tittle = models.CharField(max_length=100)
    subtittle = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photo/')
    def __str__(self):
        return self.tittle