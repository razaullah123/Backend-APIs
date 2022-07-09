from django.contrib.auth import authenticate


from django.contrib.auth.models import User
from django.http import JsonResponse

from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated,
                                        )
from rest_framework.views import APIView


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
                API URL:  http://127.0.0.1:8000/auth/registration/
                {
                    "username": "razaullah",
                    "email": "raza@yopmail.com",
                }

            Response Body:
                {
                    "result": username,
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
        """Login end user

        Example:
            Request Body:
                API URL:  http://127.0.0.1:8000/auth/sign-in/
                {
                    "username": "raza@yopmail.com",
                    "password": "pass@word"
                }
            Response Body:
                {
                    "result": "User login Successfully",
                    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InJhemFAeW9wbWFpbC5jb20iLCJ1c2VybmFtZSI6InJhemF1bGxhaCIsImlhdCI6MTY1NzMwNzgwNH0.dGOcISYWPIMskh0nhTigRtrJsawoaPwabFWo0m9Tgik",
                    "users": [
                        {
                            "id": 1,
                            "username": "razaullah",
                            "email": "raza@yopmail.com"
                        }
                    ]
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
