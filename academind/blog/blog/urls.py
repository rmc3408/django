from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home_page"),
    path('posts/', views.list, name="list_page"),
    path('posts/<slug:slug>', views.detail, name="detail_page"),
]