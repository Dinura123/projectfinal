from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about),
    path('Vehicle', views.Vehicle),
    path('contact', views.contact),
    path('signin', views.signin),
    path('signup', views.signup)
    ]