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

    return render(request, "network/index.html", {
        'posts': Post.objects.all(),
        'likes': Like.objects.all(),
        'likes_by_user': Like.objects.filter(user=request.user)
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
        post = Post.objects.get(id=post_id)
        new_like = Like(user=user, post=post)
        new_like.save()
        return JsonResponse({'message': 'OK'})

@csrf_exempt
def likes(request, post_id):
    post = Post.objects.get(id=post_id)
    data = {}
    likes = Like.objects.filter(post=post)

    for like in likes:
        data[like.id] = {
            'user': like.user.id,
            'post': like.post.id
        }
    return JsonResponse(len(data), safe=False)
