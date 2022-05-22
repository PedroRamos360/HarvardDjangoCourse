from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signin', signin, name='signin'),
    path('signup', signup, name='signup'),
    path('logout', logout_view, name='logout'),
    path('closet/', closet, name='closet'),
    path('looks', looks, name='looks'),
    path('closet/create/item', createItem, name='createItem'),
    path('closet/edit/item/<int:id>', editItem, name='editItem'),
    path('closet/create/category', createCategory, name='createCategory'),
    path('closet/delete/<int:id>', deleteClothingItem, name='deleteClothingItem')
]