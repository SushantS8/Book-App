from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()  

class BaseAPITestCase(APITestCase):
    def setUp(self):
        """Set up test user and authentication token"""
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')  # Auto-authenticate requests
