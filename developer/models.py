from django.db import models

# Create your models here.
from django.db import models


class Developer(models.Model):
    name = models.CharField(max_length=255)
    logo = models.CharField(max_length=999, blank=True)
    year_of_start = models.DateTimeField()
