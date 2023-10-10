from django.urls import path

from . import views

urlpatterns = [
    path("", views.home),
    path("<slug:slug>", views.details, name="book-details")
]