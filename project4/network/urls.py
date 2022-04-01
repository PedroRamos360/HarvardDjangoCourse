
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('like', views.like, name='like'),
    path('likes/<int:post_id>', views.likes, name='likes'),
    path('following', views.following, name='following'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    path('test', views.test, name='test')
]
