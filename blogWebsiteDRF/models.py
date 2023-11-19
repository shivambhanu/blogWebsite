from django.db import models

# Create your models here.
class Blog(models.Model):
    author = models.CharField(max_length=255)
    content = models.TextField(max_length=1000)
    date_time = models.DateTimeField(auto_now=True)
