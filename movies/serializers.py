from rest_framework import serializers
from .models import Movie, RatingChoices
from users.models import MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True)
    rating = serializers.ChoiceField(
        allow_null=True,
        choices=RatingChoices,
        default=RatingChoices.DEFAULT,
    )
    synopsis = serializers.CharField(allow_null=True)
    added_by = serializers.EmailField(max_length=127, read_only=True)

    def create(self, validated_data):
        user = validated_data.pop("user")
        validated_data["added_by"] = user.email

        return Movie.objects.create(**validated_data)


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(source="movie.title", read_only=True)
    buyed_by = serializers.EmailField(source="user.email", read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)
