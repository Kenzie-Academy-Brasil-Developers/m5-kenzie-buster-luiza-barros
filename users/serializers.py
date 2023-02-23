from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=127)
    email = serializers.EmailField(max_length=127)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(allow_null=True, default=None)
    is_employee = serializers.BooleanField(default=False)
    password = serializers.CharField(write_only=True)
    is_superuser = serializers.BooleanField(read_only=True)

    validators = [
        UniqueTogetherValidator(
            queryset=User.objects.all(),
            fields=["username", "email"],
        )
    ]

    def create(self, validated_data):
        if validated_data["is_employee"]:
            return User.objects.create_superuser(**validated_data)
        else:
            return User.objects.create_user(**validated_data)
