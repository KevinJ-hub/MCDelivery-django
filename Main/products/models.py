from django.db import models

# Create your models here.


class Food(models.Model):
    title = models.CharField(max_length=100, blank=False)
    desc = models.TextField(blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    image = models.URLField(max_length=200, blank=False)
    veg = models.BooleanField(blank=False)


class User(models.Model):
    username = models.CharField(blank=False, max_length=15)
    password = models.CharField(blank=False, max_length=50)
    email = models.EmailField(blank=False, max_length=254)
    address = models.TextField(blank=False)
