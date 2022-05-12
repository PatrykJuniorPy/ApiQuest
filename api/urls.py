from django.urls import include, path
from . import views

urlpatterns = [
    path('books/', views.books),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
