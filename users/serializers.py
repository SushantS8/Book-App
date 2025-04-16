from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    """Serializer for User Model with password hashing"""

    password = serializers.CharField(write_only=True, required=True)  # Ensure password is not returned in API response

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']  # Include password in fields

    def create(self, validated_data):
        """Override create to hash password"""
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data.get('email', '')  # Optional email field
        )
        user.set_password(validated_data['password'])  # Hash password
        user.save()
        return user
