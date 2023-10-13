from django.urls import path
from . import views


urlpatterns = [
  # path('', views.home, name='reviews-home'),
  # path('thank', views.thank, name='reviews-thank'),
  path('', views.Home.as_view(), name='reviews-home'),
  path('thank', views.Thank.as_view(), name='reviews-thank'),
  path('reviews', views.List.as_view(), name='reviews-list'),
  path('reviews/<str:user_name>', views.Detail.as_view(), name='reviews-detail'),
]
