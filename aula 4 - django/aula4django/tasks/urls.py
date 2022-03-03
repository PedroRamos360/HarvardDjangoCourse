from django.urls import path
from .views import *

app_name = 'tasks'
urlpatterns = [
    path('', index, name='index'),
    path('add', add, name='add'),
]
