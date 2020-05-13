from django.db import models

# Create your models here.
from django.db import models

from developer.models import Developer


class GameCategory(models.Model):
    name = models.CharField(max_length=255)


class Game(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=999, blank=True)
    description = models.CharField(max_length=999, blank=True)
    category = models.ForeignKey(GameCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    on_sale = models.BooleanField()
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class GameImage(models.Model):
    image = models.CharField(max_length=999)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)


