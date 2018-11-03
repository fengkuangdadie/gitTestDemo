from django.db import models


class Dog(models.Model):
    d_name = models.CharField(max_length=32, unique=True)
    d_legs = models.IntegerField(default=4)