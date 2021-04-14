from django.db import models

# Create your models here.


class Food(models.Model):
    title = models.CharField(max_length=100, blank=False)
    desc = models.TextField(blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    image = models.URLField(max_length=200, blank=False)
    veg = models.BooleanField(blank=False)

