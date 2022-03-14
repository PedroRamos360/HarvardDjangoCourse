from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>', views.get_article, name='get_article'),
    path('search', views.search, name='search'),
    path('create', views.create_article, name='create_article'),
    path('edit/<str:title>', views.edit_article, name='edit_article')
]
