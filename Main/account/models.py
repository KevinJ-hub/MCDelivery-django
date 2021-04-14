from django.contrib.auth.forms import UsernameField
from django.db import models


class my_user(models.Model):
    username = models.CharField(blank=False, max_length=15)
    address = models.TextField(blank=False)
    email = models.EmailField(blank=False, max_length=254, unique=True)
    password = models.CharField(blank=False, max_length=50)
    # user_cart = models.ManyToManyField()

