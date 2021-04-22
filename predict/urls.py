from django.urls import path
from . import views

app_name = "predict"

urlpatterns = [
    path('', views.predict, name='classifier'),
    path('', views.predict_chances, name='submit_prediction'),
    path('', views.view_results, name='results'),
]
