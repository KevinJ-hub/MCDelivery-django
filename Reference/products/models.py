from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class Food(models.Model):
    title = models.CharField(max_length=100, blank=False)
    desc = models.TextField(blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    image = models.URLField(max_length=200, blank=False)
    veg = models.BooleanField(blank=False)


# class User(models.Model):
#     username = models.CharField(blank=False, max_length=15)
#     password = models.CharField(blank=False, max_length=50)
#     email = models.EmailField(blank=False, max_length=254)
#     address = models.TextField(blank=False)


class Cart(models.Model):
    item = models.ForeignKey(Food, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
