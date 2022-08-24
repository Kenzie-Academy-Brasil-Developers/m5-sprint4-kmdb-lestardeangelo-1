from rest_framework import serializers
from django.core.exceptions import ValidationError

from .models import Review
from users.models import User


class CriticSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class ReviewSerializer(serializers.ModelSerializer):
    critic = CriticSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = ['id', 'stars', 'review', 'spoilers', 'movie_id', 'critic', 'recomendation']
        read_only_fields = ['movie_id']
        extra_kwargs = {'stars': {'min_value': 1, 'max_value': 10}}
    

    def create(self, validated_data):
        user = validated_data.pop("critic")
        movie = validated_data.pop("movie_id")

        is_duplicated = Review.objects.filter(movie_id=movie.id, critic=user)

        if is_duplicated:
            raise ValidationError({'detail': 'Review already exists.'})

        review = Review.objects.create(**validated_data, critic=user, movie_id=movie)

        return review