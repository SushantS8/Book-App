from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """Serializes the Book Model"""
    class Meta:
        model = Book
        fields = '__all__'
