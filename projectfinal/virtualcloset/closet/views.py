from platform import uname
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
    q = request.GET.get('q')
    try:
        category = ClothingCategory.objects.get(id=q)
        clothes = ClothingItem.objects.filter(user=request.user, category=category)
    except:  
        clothes = ClothingItem.objects.filter(user=request.user)
    return render(request, 'closet/closet.html', {
        'clothes': clothes,
        'categories': ClothingCategory.objects.filter(user=request.user)
    })


def looks(request):
    looks = Look.objects.filter(user=request.user)

    return render(request, 'closet/looks.html', {
        'looks': looks
    })


def createItem(request):
    if request.method == "POST":
        name = request.POST['name']
        image = request.FILES['image']
        action = f'/closet/edit/item/{id}'
        try:
            category_id = request.POST['category_id']
            category = ClothingCategory.objects.get(id=category_id)
        except:
            category = None
    
        new_clothing_item = ClothingItem(image=image, user=request.user, name=name, category=category)
        new_clothing_item.save()

        return HttpResponseRedirect('/closet')
        
        
    return render(request, 'closet/createItem.html', {
        'categories': ClothingCategory.objects.filter(user=request.user),
    })


def editItem(request, id):
    if request.method == "POST":
        name = request.POST['name']
        try:
            category_id = request.POST['category_id']
            category = ClothingCategory.objects.get(id=category_id)
        except:
            category = None


        edited_clothing_item = ClothingItem.objects.get(id=id)
        edited_clothing_item.name = name
        edited_clothing_item.category = category

        try: 
            image = request.FILES['image']
            edited_clothing_item.image = image
        except:
            pass

        edited_clothing_item.save()

        print("Redirecting to closet...")
        return HttpResponseRedirect('/closet')
    
    clothingItem = ClothingItem.objects.get(id=id)

    return render(request, 'closet/editItem.html', {
        'categories': ClothingCategory.objects.filter(user=request.user),
        'clothingItem': clothingItem,
        'id': id
    })


def createCategory(request):
    if request.method == "POST":
        name = request.POST['name']
    
        new_category = ClothingCategory(user=request.user, name=name)
        new_category.save()

        return HttpResponseRedirect('/closet')
        
    return render(request, 'closet/createCategory.html')


def deleteClothingItem(request, id):
    clothtingItem = ClothingItem.objects.get(id=id)
    if (clothtingItem.user == request.user):
        clothtingItem.delete()

    return HttpResponseRedirect(reverse('home'))


def createLook(request):
    if request.method == "POST":
        name = request.POST["name"]
        image = request.FILES['image']
        user = request.user
        newLook = Look(user=user, name=name, image=image)
        newLook.save()

        i = 0
        while True:
            try:
                clothIndex = request.POST[("clothingItem_id" + str(i))]
                newLook.clothes.add(clothIndex)
                newLook.save()
            except:
                break
            i += 1
    

        

    return render(request, 'closet/createLook.html', {
        'clothes': ClothingItem.objects.filter(user=request.user),
    })
