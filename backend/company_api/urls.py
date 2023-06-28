from django.urls import path
from .views import CompanyDetail, CompanyList

urlpatterns = [
    path("<int:pk>", CompanyDetail.as_view(), name='update_create'),
    path("", CompanyList.as_view(), name='list'),
]