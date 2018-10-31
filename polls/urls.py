from django.urls import path

from . import views

urlpatterns = [
    path('plist/<str:pid>/<str:ipa_id>', views.plist),
]
