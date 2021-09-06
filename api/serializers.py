from rest_framework import serializers
from .models import Books


class BooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = (
            'id', 'title', 'authors', 'published_date', 'categories', 'average_rating', 'rating_count', 'thumbnail'
        )
