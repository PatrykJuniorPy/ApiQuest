import requests
from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def books(request):
    r = requests.get("https://www.googleapis.com/books/v1/volumes?q=Hobbit")
    return Response(r.json())
