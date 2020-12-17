from django.urls import path
from . import views

urlpatterns = [
    path('', views.djform, name="djform")
]