from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('auctions/<int:id>', views.auction, name='auction'),
    path('categories', views.categories, name='categories'),
    path('watchlist', views.watchlist, name='watchlist'),
    path('create_listing', views.create_listing, name='create_listing'),
    path('comment', views.comment, name='comment'),
    path('bid', views.bid, name='bid')
]
