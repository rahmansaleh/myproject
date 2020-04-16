from django.db import models
from django.conf import settings
import datetime

class Post(models.Model):
    title = models.CharField(max_length=200, default='')
    slug = models.SlugField(unique=True, default='')
    image = models.ImageField(upload_to='post/%Y/%m', blank=True)
    content = models.TextField(default='')
    draft = models.BooleanField(default=True)
    publish = models.DateField(auto_now=False, auto_now_add=False, default=datetime.date.today)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

# Create your models here.
