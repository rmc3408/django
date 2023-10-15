from django.urls import path
from . import views

urlpatterns = [
    path("", views.CreateProfile.as_view()),
    path("list", views.ListProfile.as_view())
]