from django.db import models

from developer.models import Developer
from game.models import Game


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=750)
    email = models.CharField(max_length=500, unique=True)
    phoneno = models.CharField(max_length=50)


class Purchases(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_game = models.ForeignKey(Game, on_delete=models.CASCADE)
    dateofpurchase = models.DateTimeField(auto_now=True)
    amount = models.FloatField


class Basket(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_game = models.ForeignKey(Game, on_delete=models.CASCADE)
