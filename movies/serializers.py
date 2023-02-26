from rest_framework import serializers
from .models import Movie, RatingChoices


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
