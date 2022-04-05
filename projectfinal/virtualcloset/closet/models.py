from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class ClothingCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)


class LookCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)


class ClothingItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='clothes/')
    category = models.ForeignKey(ClothingCategory, on_delete=models.CASCADE, default=None, blank=True)


class Look(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='looks/')
    category = models.ForeignKey(LookCategory, on_delete=models.CASCADE, default=None, blank=True)




