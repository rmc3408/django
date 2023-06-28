from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit\<str:id>', views.form, name='edit'),
    path('<str:id>', views.room, name='room'),
    
]
