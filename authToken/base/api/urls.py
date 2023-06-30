from django.urls import include, path
from .views import UserViewSet, getRouters, getNotes
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('', getRouters, name='main'),
    path('notes/', getNotes, name='notes'),
    path('users/<int:pk>', UserViewSet.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # API-AUTH will Adding login to the Browsable API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]