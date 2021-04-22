from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('classifier', views.SentimentView)



urlpatterns = [
    path('', views.demo, name='demo'),
    path('api', include(router.urls)),
    path('manager', views.manager, name='manager'),
    ]
