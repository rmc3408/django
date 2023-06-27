from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # path("hello", views.hello, name="index"),
    path("", TemplateView.as_view(template_name='company/index.html')),
]