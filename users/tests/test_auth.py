from django.contrib.auth import get_user_model
from rest_framework import status
from users.tests.test_base import BaseAPITestCase

User = get_user_model()

class AuthTestCase(BaseAPITestCase):

    def test_register_user(self):
        """Test user registration API"""
        data = {"username": "newuser", "password": "newpassword"}
        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        """Test user login API and token generation"""
        data = {"username": "testuser", "password": "testpassword"}
        response = self.client.post("/api/token/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)  # Check if access token is returned

    def test_access_protected_route(self):
        """Test access to protected route with valid JWT token"""
        response = self.client.get("/api/protected-endpoint/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_access_protected_route_without_token(self):
        """Test access to protected route without authentication"""
        self.client.credentials()  # Remove token
        response = self.client.get("/api/protected-endpoint/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # Expect Unauthorized
