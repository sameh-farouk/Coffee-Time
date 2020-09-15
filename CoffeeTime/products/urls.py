from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'coffee-machines', views.CoffeeMachineViewSet)
router.register(r'coffee-pods', views.CoffeePodViewSet)

urlpatterns = [
    path('', include(router.urls)),
]