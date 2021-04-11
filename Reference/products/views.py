from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.


def home(req, *args, **kwargs):
    return render(req, "base.html")


def cart(req, *args, **kwargs):
    return HttpResponse("Cart")


def profile(req, *args, **kwargs):
    return HttpResponse("Profile")


def signup(req, *args, **kwargs):
    form = MyAccountForm(req.POST)
    if form.is_valid():
        User.objects.create(**form.cleaned_data)
        messages.success(
            req, 'Signed up successfully', extra_tags='alert')
        return redirect("home")
    else:
        print(form.errors)

    context = {
        "forms": form
    }
    return render(req, "registration/signup.html", context)
