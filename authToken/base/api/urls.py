from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, getRouters
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)


urlpatterns = [
    path('', getRouters, name='main'),
    
    path('auth/', include(router.urls), name='auth'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # API-AUTH will Adding login to the Browsable API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]