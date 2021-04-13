from django.shortcuts import render
from .models import Food

# from django.http import HttpResponse

# Create your views here.


def home(req, *args, **kwargs):
    obj = list(Food.objects.all())
    return render(req, "home.html", {"obj": obj})


def login(req, *args, **kwargs):
    return render(req, "login.html")


def cart(req, *args, **kwargs):
    return render(req, "cart.html")


def profile(req, *args, **kwargs):
    return render(req, "profile.html")
