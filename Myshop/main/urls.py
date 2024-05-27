from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrate, name='registrate'),
    path('login1', views.login, name='login1'),
    path('home', views.main, name='home'),
    path('rewiew', views.rewiew, name='rewiew'),
    path('basket', views.basket, name='basket'),
    path('addRewiew', views.addRewiew, name='addRewiew'),
]