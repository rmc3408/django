from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('create', views.create, name='create'),
    path('<str:id>', views.room, name='room'),
    path('edit/<str:id>', views.update, name='edit'),
    path('delete/<str:id>', views.delete, name='delete'),
]
