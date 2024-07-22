from rest_framework import serializers
from .models import Audiobook, Author, Genre, Review

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class AudiobookMiniSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
 
    average_rating = serializers.FloatField(read_only=True)
    cover_image = serializers.ImageField(read_only=True,use_url=True)

    class Meta:
        model = Audiobook
        fields = ['id', 'title', 'author', 'cover_image', 'average_rating']

class AudiobookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    genre = GenreSerializer(many=True)
    average_rating = serializers.FloatField(read_only=True)
    cover_image = serializers.ImageField(read_only=True,use_url=True)

    class Meta:
        model = Audiobook
        fields = ['id', 'title', 'author', 'cover_image', 'description', 'genre', 'average_rating','seo_title','seo_description','seo_keywords']

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'rating', 'review_text', 'created_at']
class ReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id', 'audiobook', 'rating', 'review_text']