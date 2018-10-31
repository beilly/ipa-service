from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('plist/<str:ipa_id>', views.plist),
]
