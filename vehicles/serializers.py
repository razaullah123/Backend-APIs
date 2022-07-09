from rest_framework import serializers

from .models import Category, Car


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['color', 'model', 'register_num', 'category','register_cars']

    register_cars = serializers.SerializerMethodField(method_name='register', read_only=True)

    def register(self, car: Car):
        return Car.objects.all().count()




