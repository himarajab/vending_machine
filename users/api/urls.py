from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='users-api'
urlpatterns = [
    path('register', views.UserCreate.as_view()),
    path('login/', auth_views.LoginView.as_view(template_name='rest_framework/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
