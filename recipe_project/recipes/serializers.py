# recipes/serializers.py
from rest_framework import serializers
from .models import Recipe, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('user', 'text', 'rating' ,'ingredients')

class RecipeSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'description', 'rating', 'reviews' , 'ingredients')
