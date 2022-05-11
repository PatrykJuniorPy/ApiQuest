from rest_framework import viewsets
from .serializers import BooksSerializer
from .models import Books
from rest_framework.response import Response


# Create your views here.

class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


# def read_books(request):
#     r = requests.get(
#         "https://www.googleapis.com/books/v1/volumes?q=Hobbit")
#     Response(r.json())


# class HobbitView(viewsets.ModelViewSet):
