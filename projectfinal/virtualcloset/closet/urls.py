from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signin', signin, name='signin'),
    path('signup', signup, name='signup'),
    path('logout', logout_view, name='logout'),
    path('closet/', closet, name='closet'),
    path('looks', looks, name='looks'),
    path('schedule', schedule, name='schedule'),
    path('trip', trip, name='trip'),
    path('closet/create/item', createItem, name='createItem'),
    path('closet/create/category', createCategory, name='createCategory'),
]