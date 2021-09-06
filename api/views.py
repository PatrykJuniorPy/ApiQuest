from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BooksSerializer
from .models import Books


# Create your views here.
class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all().order_by('title')
    serializer_class = BooksSerializer
