from django.urls import path
from django.urls import include
from . import views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView
)

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about),
    path('Vehicle', views.Vehicle),
    path('contact', views.contact),
    path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('dashboard', views.dashboard, name='dashboard')
    ]