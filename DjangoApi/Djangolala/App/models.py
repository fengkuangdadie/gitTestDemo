from django.db import models

class Blog(models.Model):
    b_title = models.CharField(max_length=128)
