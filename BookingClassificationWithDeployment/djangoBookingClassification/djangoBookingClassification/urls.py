from django.urls import path
from MlAPI import views

urlpatterns = [
    path('predict/', views.predictor, name='predict'),
]