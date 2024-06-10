from rest_framework.serializers import ModelSerializer
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
    class Meta:
        model = Book
        fields = '__all__'