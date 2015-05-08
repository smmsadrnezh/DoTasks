from django.db import models

from lists.models import Lists


# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=200)
    list = models.ForeignKey(Lists)