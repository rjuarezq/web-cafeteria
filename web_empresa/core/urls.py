from django.urls import path
from . import views

urlpatterns = [
    #Paths solo core
    path('', views.home, name="index"),
    path('about/', views.about, name="about"),
    path('store/', views.store, name="store"),
    path('contact/', views.contact, name="contact"),
    path('blog/', views.blog, name="blog"),
]