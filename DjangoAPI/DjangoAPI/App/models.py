from django.db import models


class Boom(models.Model):
    b_title = models.CharField(max_length=128)