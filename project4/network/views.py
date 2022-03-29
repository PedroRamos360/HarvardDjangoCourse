from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json


from .models import *


def index(request):
    if request.method == "POST":
        user = request.user
        body = request.POST['body']
        new_post = Post(user=user, body=body)
        new_post.save()
    
    try:
        posts_liked_by_user = []
        likes_from_user = Like.objects.filter(user=request.user)
        for like in likes_from_user:
            posts_liked_by_user.append(like.post)
    except:
        posts_liked_by_user = None

    return render(request, "network/index.html", {
        'posts': Post.objects.all(),
        'posts_liked_by_user': posts_liked_by_user
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


@csrf_exempt
@login_required
def like(request):
    if request.method == "POST":
        user = request.user
        data = request.body.decode('utf-8')
        body = json.loads(data)
        post_id = body['post_id']
        like = body['like']
        print(like)
        print(type(like))
        post = Post.objects.get(id=post_id)
        if like:
            new_like = Like(user=user, post=post)
            new_like.save()
        else:
            previous_like = Like.objects.get(user=user, post=post)
            previous_like.delete()
        return JsonResponse({'message': 'OK'})

@csrf_exempt
def likes(request, post_id):
    post = Post.objects.get(id=post_id)
    likes = Like.objects.filter(post=post)     

    return JsonResponse(len(likes), safe=False)


def following(request):
    return render(request, 'network/following.html')

def profile(request, user_id):
    user_from_page = User.objects.get(id=user_id)
    return render(request, 'network/profile.html', {
        'user_from_page': user_from_page,
        'posts': Post.objects.filter(user=user_from_page)
    })
