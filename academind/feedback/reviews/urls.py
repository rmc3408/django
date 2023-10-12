from django.urls import path
from . import views


urlpatterns = [
  # path('', views.home, name='reviews-home'),
  path('', views.Home.as_view(), name='home'),
  path('thank', views.thank, name='reviews-thank')
]