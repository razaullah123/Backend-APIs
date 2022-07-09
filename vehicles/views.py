from user.utils import JWTAuthentication

from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from django.core.mail import send_mail

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import Category, Car
from .serializers import CategorySerializer, CarSerializer


class CategoryViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination


class CarViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Car.objects.select_related('category').all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category_id', 'color', 'model', 'register_num']
    search_fields = ['color']
    ordering_fields = ['model', 'register_num']
    pagination_class = PageNumberPagination


def send_email(request,id):
    email = User.objects.filter(id=id)
    send_mail('user confirmation mail', 'welcome you are succesfuly registerd', 'iamharisgul@gmail.com', ['iamharisgul@gmail.com'])
    Response("email send")




