from django.urls import path
from . import views

urlpatterns = [
    #Paths solo services
    path('', views.services, name="services"),
]