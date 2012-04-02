
from django.db import models
class ShortUrl(models.Model):
    ourl = models.CharField(max_length=200)
    code=models.CharField(max_length=200)
    surl=models.CharField(max_length=200)

# Create your models here.
