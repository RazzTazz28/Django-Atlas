from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Person
from django.contrib.auth import authenticate, login, logout
from .models import NewUser


# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('profiles')
    else:
        if request.method == 'POST':
            form_one = Person(request.POST)
            if form_one.is_valid():
                form_one.save()

                username = form_one.cleaned_data.get("username")

                messages.success(request, f"Account created for {username}!")
                return redirect("login_user")

        else:
            form_one = Person()

        return render(request, "accounts/register.html", {"form_one": form_one})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('profiles')
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, ("Login Successfull."))
                return redirect("profiles")

            else:
                messages.success(request, ("Username or password are incorect."))
                return redirect("login_user")
        else:
            return render(request, "accounts/login_user.html", {})
