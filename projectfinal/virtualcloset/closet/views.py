from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse


from .models import *


def home(request):
    return render(request, 'closet/home.html')


def signin(request):
    return render(request, 'closet/signin.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmation = request.POST['confirmation']

        if password != confirmation:
            return render(request, 'closet/signup.html', {
                'message': 'Passwords must match!'
            })
        
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, 'closet/signup.html', {
                'message': 'Username already taken!'
            })
        
        login(request, user)
        return HttpResponseRedirect(reverse("home"))


    return render(request, 'closet/signup.html')

