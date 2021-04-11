from django.shortcuts import render
from django.http import HttpResponse
from .models import Food

# Create your views here.


def home(req, *args, **kwargs):
    return HttpResponse("Home")


def login(req, *args, **kwargs):
    return HttpResponse("Login")


def cart(req, *args, **kwargs):
    return HttpResponse("Cart")


def profile(req, *args, **kwargs):
    return HttpResponse("Profile")
