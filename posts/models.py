from django.db import models
from django.conf import settings
import datetime

class Post(models.Model):
    title = models.CharField(max_length=200),
    slug = models.SlugField(unique=True),
    image = models.ImageField(upload_to='post/%Y/%m', blank=True),
    content = models.TextField(),
    draft = models.BooleanField(default=False),
    publish = models.DateField(auto_now=False, auto_now_add=False),
    updated = models.DateTimeField(auto_now=True, auto_now_add=False),
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True),

    def __str__(self):
        return self.title

# Create your models here.
