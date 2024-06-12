from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        
class BookSerializer(ModelSerializer):
        category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
        pdf_file = serializers.FileField(required=False, allow_null=True)
        class Meta:
            model = Book
            fields = '__all__'