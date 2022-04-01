from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from itertools import chain
from django.core.paginator import Paginator


from .models import *


@csrf_exempt
def index(request):
    if request.method == "POST":
        user = request.user
        body = request.POST['body']
        new_post = Post(user=user, body=body)
        new_post.save()

    if request.method == "PUT":
        data = request.body.decode('utf-8')
        body = json.loads(data)
        post_id = body['post_id']
        content = body['body']
        post = Post.objects.get(id=post_id)
        if post.user == request.user: # Safety verification
            post.body = content
            post.save()

    try:
        posts_liked_by_user = []
        likes_from_user = Like.objects.filter(user=request.user)
        for like in likes_from_user:
            posts_liked_by_user.append(like.post)
    except:
        posts_liked_by_user = None
    
    posts = Post.objects.all().order_by('timestamp').reverse()
    paginator = Paginator(posts, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "network/index.html", {
        'posts': page_obj,
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
        post = Post.objects.get(id=post_id)
        if like:
            new_like = Like(user=user, post=post)
            new_like.save()
            post.likes = post.likes + 1
            post.save()
        else:
            previous_like = Like.objects.get(user=user, post=post)
            previous_like.delete()
            post.likes = post.likes - 1
            post.save()
        return JsonResponse({'message': 'OK'})

@csrf_exempt
def likes(request, post_id):
    post = Post.objects.get(id=post_id)
    likes = Like.objects.filter(post=post)     

    return JsonResponse(len(likes), safe=False)


def following(request):
    follower_objects = Follower.objects.filter(user_following=request.user)
    users_following = []
    for follower_object in follower_objects:
        users_following.append(follower_object.user_followed)

    posts = []
    for user in users_following:
        posts_from_user = Post.objects.filter(user=user).order_by('timestamp').reverse()
        posts.append(posts_from_user)

    result_list = list(chain(*posts))
    def sort_posts(object):
        return object.timestamp

    result_list.sort(key=sort_posts, reverse=True)

    try:
        posts_liked_by_user = []
        likes_from_user = Like.objects.filter(user=request.user)
        for like in likes_from_user:
            posts_liked_by_user.append(like.post)
    except:
        posts_liked_by_user = None
    

    return render(request, 'network/following.html', {
        'posts': result_list,
        'posts_liked_by_user': posts_liked_by_user
    })

@csrf_exempt
def profile(request, user_id):
    if request.method == "POST":
        data = request.body.decode('utf-8')
        body = json.loads(data)
        follow = body['follow']
        
        user_following = request.user
        user_followed = User.objects.get(id=user_id)
        if follow:
            new_follower = Follower(user_following=user_following, user_followed=user_followed)
            new_follower.save()
            user_followed.followers = user_followed.followers + 1
            user_followed.save()
            user_following.following = user_following.following + 1
            user_following.save()
        else:
            previous_follower = Follower.objects.get(user_following=user_following, user_followed=user_followed)
            previous_follower.delete()
            user_followed.followers = user_followed.followers - 1
            user_followed.save()
            user_following.following = user_following.following - 1
            user_following.save()


    user_followed_page_user = False
    try:
        follower_objects_followed_by_user = Follower.objects.filter(user_following=request.user)
        users_followed_by_user = []
        for follower in follower_objects_followed_by_user:
            users_followed_by_user.append(follower.user_followed)

        user_followed = User.objects.get(id=user_id)
        if user_followed in users_followed_by_user:
            user_followed_page_user = True 
    except:
        pass

    try:
        posts_liked_by_user = []
        likes_from_user = Like.objects.filter(user=request.user)
        for like in likes_from_user:
            posts_liked_by_user.append(like.post)
    except:
        posts_liked_by_user = None

    user_from_page = User.objects.get(id=user_id)
    return render(request, 'network/profile.html', {
        'user_from_page': user_from_page,
        'posts': Post.objects.filter(user=user_from_page).order_by('timestamp').reverse(),
        'user_followed_page_user': user_followed_page_user,
        'posts_liked_by_user': posts_liked_by_user
    })

def test(request):
    return render(request, 'network/test.html')
