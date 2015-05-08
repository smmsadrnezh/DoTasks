from django.db import models

# Create your models here.
class Lists(models.Model):
    title=models.CharField(max_length=200)