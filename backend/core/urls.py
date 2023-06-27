from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('company/', include('company.urls')),
    path('company/api/', include('company_api.urls')),
    path('admin/', admin.site.urls),
]
