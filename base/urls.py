from django.urls import path, include
from .views import *
urlpatterns = [
    path('category/',CategoryApiView.as_view({'get':'list','post':'create'}),name='category'),
    path('category/<int:pk>/',CategoryApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='category'),
    path('author/',AuthorApiView.as_view({'get':'list','post':'create'}),name='author'),
    path('author/<int:pk>/',AuthorApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='author'),
    path('book/',BookApiView.as_view({'get':'list','post':'create'}),name='book'),
    path('book/<int:pk>/',BookApiView.as_view({'get':'retrieve','put':'update','delete':'destroy'}),name='book'),
]