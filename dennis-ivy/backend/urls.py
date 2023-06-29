from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('api.urls'), name='api'),
    path('admin/', admin.site.urls),
]
