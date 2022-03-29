from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    body = models.CharField(max_length=280)
    likes = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.CharField(max_length=280)
    timestamp = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Follower(models.Model):
    user_following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_following')
    user_followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_followed')
