from django.db import models


class Book(models.Model):

    b_name = models.CharField(max_length=32)
    b_price = models.FloatField(default=1)


class Game(models.Model):

    g_name = models.CharField(max_length=32)
    g_price = models.FloatField(default=0)