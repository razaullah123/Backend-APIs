
import json
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated,
                                        )


from backendapis import settings
from user.serializers import (
    LoginSerializer,
    RegistrationSerializer,

)
from user.utils import generate_access_token


class RegistrationView(APIView):
    """User registration APIView"""

    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        """Register a new user.

        Example:
            Request Body:
                API URL: http://baseurl/users/registration/
                {
                    "fullname": "Shakeel Afridi",
                    "phone_number": "+92316151****",
                    "email": "shakeel@domin.com",
                    "password": "pass@word",
                    "city": "Islamabad",
                }

            Response Body:
                {
                    "success": true,
                    "payload": {},
                    "message": "OTP sent successfully."
                }

        """
        serializer_registration = self.serializer_class(data=request.data)
        if not serializer_registration.is_valid():
            return JsonResponse({'result': serializer_registration.errors})
        user = serializer_registration.save()
        return JsonResponse({"result": user.username})


class SignInView(APIView):
    """User Sign in APIView
    """

    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        # User.objects.filter(phone_number="+923420202688").delete()
        """Login end user

        Example:
            Request Body:
                API URL: http://users/sign-in/
                {
                    "phone_number": "+92316151***",
                    "password": "pass@word"
                }
            Response Body:
                {
                    "success": true,
                    "payload": {
                        "token": "jwt-token"
                    },
                    "message": "Logged in successfully."
                }
        """

        serializer_login = self.serializer_class(data=request.data)
        if not serializer_login.is_valid():
            return JsonResponse({'result': serializer_login.errors})

        user = authenticate(
            username=request.data.get("username"),
            password=request.data.get("password"),
        )
        if not user:
            return JsonResponse({'result': "User not found"})
        jtoken = generate_access_token(user)
        user_list = []
        for user in User.objects.all():
            user_list.append({
                'id':user.id,
                'username':user.username,
                'email':user.email
            })

        return JsonResponse({'result': "User login Successfully", 'token': jtoken, 'users':user_list})
