import requests
from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import Books
from api.serializers import BooksSerializer


@api_view(['GET'])
def books(request):
    r = requests.get("https://www.googleapis.com/books/v1/volumes?q=Hobbit")
    return Response(r.json())


@csrf_exempt
def books_list(request):
    """
    List all code books, or create a new book

    """
    if request.method == 'GET':
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BooksSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
# def books_detail(request, pk):
#     """
#     Retrieve, update or delete a code book.
#     """
#     try:
#         books = Books.objects.get(pk=pk)
#     except Books.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = BooksSerializer(books)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = BooksSerializer(books, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         books.delete()
#         return HttpResponse(status=204)
