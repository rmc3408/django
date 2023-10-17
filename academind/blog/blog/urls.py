from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home_page"),
    path('posts/<slug:slug>', views.Detail.as_view(), name="detail_page"),
    path('posts/', views.List.as_view(), name="list_page" ),
    path("read-later", views.ReadLaterView.as_view(), name="read-later")
]