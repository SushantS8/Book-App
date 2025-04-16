from django.urls import path
from .api_views import UserCreateView, UserDetailView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # API Endpoints
    path('api/register/', UserCreateView.as_view(), name='api-user-register'),
    path('api/user/<int:pk>/', UserDetailView.as_view(), name='api-user-detail'),
    # path('api/user/<int:pk>/', UserUpdateView.as_view(), name='api-user-update'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login API
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh Token
]
 