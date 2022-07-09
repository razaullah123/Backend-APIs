from django.core.mail import send_mail
from django.contrib.auth.models import User

from rest_framework import serializers

from backendapis.settings import (EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_HOST, EMAIL_PORT)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(label=("email"), write_only=True)
    username = serializers.CharField(label=("usernmae"), write_only=True)
    password = serializers.CharField(
        label=("password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "username",
        ]
        extra_kwargs = {"password": {"read_only": True}}

    def create(self, validated_data):
        user, is_created = User.objects.update_or_create(
            email=validated_data["email"],\
            username = validated_data["username"]
        )
        password = str(User.objects.make_random_password(length=6))
        user.set_password(password)
        user.save()
        try:
            send_mail("Ropstam User Password: ", password, EMAIL_HOST_USER, [user.email])
        except Exception as e:
            print(e)
        return user
