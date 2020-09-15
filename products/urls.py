from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.get_api_root_view().cls.__name__ = "CoffeeTime Restful Web Service"
router.get_api_root_view().cls.__doc__ = "API to work with CoffeeTime, an e-commerce mobile application"

router.register(r'api/coffee-machines', views.CoffeeMachineViewSet)
router.register(r'api/coffee-pods', views.CoffeePodViewSet)

urlpatterns = [
    path('', include(router.urls)),

]