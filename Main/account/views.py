from django.shortcuts import render, redirect
from .forms import my_registration_form
from .models import my_user


def registration_view(req, *args, **kwargs):
    context = {}
    if req.POST:
        form = my_registration_form(req.POST)
        if form.is_valid():
            try:
                my_user.objects.get(email=form.cleaned_data.get("email"))
            except:
                my_user.objects.create(**form.cleaned_data)
                return redirect("home")
            else:
                context["registration_form"] = form
                context["error"] = "Email ID is already registered"
                return render(req, "register.html", context)
        else:
            context["registration_form"] = form
    else:
        form = my_registration_form()
        context["registration_form"] = form
    return render(req, "register.html", context)
