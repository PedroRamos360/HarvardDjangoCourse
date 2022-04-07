from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse


from .models import *


def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/closet')
    return render(request, 'closet/home.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, 'closet/signin.html', {
                'message': 'Invalid username and/or password'
            })
        
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


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def closet(request):
    clothes = ClothingItem.objects.filter(user=request.user)
    return render(request, 'closet/closet.html', {
        'clothes': clothes
    })


def looks(request):
    return render(request, 'closet/looks.html')


def schedule(request):
    return render(request, 'closet/schedule.html')


def trip(request):
    return render(request, 'closet/trip.html')


def createItem(request):
    if request.method == "POST":
        name = request.POST['name']
        image = request.POST['image']
        category = ClothingCategory.objects.all()[0]
    
        new_clothing_item = ClothingItem(user=request.user, name=name, image=image, category=category)
        new_clothing_item.save()

        return HttpResponseRedirect('/closet')

        
    return render(request, 'closet/createItem.html')

