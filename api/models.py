from django.db import models

# Create your models here.


class films(models.Model):
    title = models.CharField(max_length=100)
    title_rus = models.CharField(max_length=100)
    description_rus = models.CharField(max_length=400)
    imdb = models.DecimalField(max_digits=4, decimal_places=2)
