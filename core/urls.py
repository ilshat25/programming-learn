from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('path', views.get_path, name='get_path'),
    path('level', views.get_level, name='get_level')
]
