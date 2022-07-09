from django.urls import path, include

from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('category', views.CategoryViewSet)
router.register('car', views.CarViewSet, basename='car')


urlpatterns = [
    path('', include(router.urls)),
    path('sendemail/<int:id>', views.send_email, name='sendemail'),

]
