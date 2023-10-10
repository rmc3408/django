from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.listMonths, name="named-list"),
    path('<int:month>', views.monthly_byNum),
    path('<str:month>', views.monthly, name="named-month"),
]