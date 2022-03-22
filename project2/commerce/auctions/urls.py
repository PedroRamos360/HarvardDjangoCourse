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
    path('your_listings', views.your_listings, name='your_listings'),
    path('create_listing', views.create_listing, name='create_listing'),
    path('comment', views.comment, name='comment'),
    path('bid', views.bid, name='bid'),
    path('endauction', views.endauction, name='endauction'),
]
