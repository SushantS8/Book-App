from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class UserCreateView(generics.CreateAPIView):
    """API endpoint for user registration"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny] # Anyone can register

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint for retrieving or updating user details"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated] # Only logged-in users can access

# class UserUpdateView(generics.RetrieveUpdateAPIView):
#     """API to retrieve or update a user"""
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

# JWT Login View (Overrides Default TokenObtainPairView)
class CustomTokenObtainPairView(TokenObtainPairView):
    """Custom JWT authentication view"""
    pass