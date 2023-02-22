from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=127)
    email = serializers.EmailField(max_length=127, unique=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(null=True)
    is_employee = serializers.BooleanField(null=True, default=False)
    password = serializers.CharField(write_only=True)
    is_superuser = serializers.BooleanField(read_only=True)

    validators = [
        UniqueTogetherValidator(
            queryset=User.objects.all(), fields=["email", "username"]
        )
    ]

    def create(self, validated_data):
        if validated_data.is_employee:
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)
