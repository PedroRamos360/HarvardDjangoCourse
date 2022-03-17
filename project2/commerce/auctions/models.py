from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.FloatField()
    def __str__(self):
        return f'{self.user}: {self.price}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=1024)

    def __str__(self):
        return f'{self.user}: {self.comment}'


class AuctionList(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=2048, default=None, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}: {self.name}'


class WatchlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    auction_list = models.ForeignKey(AuctionList, on_delete=models.CASCADE)


