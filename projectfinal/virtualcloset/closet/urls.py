from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signin', signin, name='signin'),
    path('signup', signup, name='signup'),
    path('logout', logout_view, name='logout'),
]