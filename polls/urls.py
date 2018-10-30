from django.urls import path

from . import views

urlpatterns = [
    path('plist', views.plist, name='index'),
    path('', views.index, name='index'),
]