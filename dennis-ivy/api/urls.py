from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('notes/', views.getNotes, name='notes'),
    path('notes/create', views.createNote, name='create'),
    path('notes/delete/<str:id>', views.deleteNote, name='delete'),
    path('notes/update/<str:id>', views.updateNote, name='update'),
    path('notes/<str:id>', views.getNote, name='note'),
]