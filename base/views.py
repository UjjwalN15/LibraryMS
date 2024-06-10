from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import *
# Create your views here.

class CategoryApiView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class AuthorApiView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
class BookApiView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
