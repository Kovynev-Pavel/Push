from django.urls import path
from . import views

urlpatterns = [
    path('katalog', views.katalog, name='katalog'),
    path('category/<int:pk>/', views.products, name='tovars'),
]