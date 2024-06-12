from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser
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
    parser_classes = (MultiPartParser, FormParser)
    filterset_fields = ['name','author','category']
    search_fields = ['name','description']
