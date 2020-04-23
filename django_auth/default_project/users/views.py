from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    if request.user.is_authenticated:
        context = {
            "user": request.user
        }
        return render(request, "users/user.html", context)
    else:
        return render(request, "users/login.html", {"message": None})


def login_view(request):
    print(request.POST)
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "users/login.html", {"message": "Invalid credentials"})


def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})
