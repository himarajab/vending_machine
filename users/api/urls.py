from django.urls import path
from . import views
app_name='users-api'
urlpatterns = [
    path('register', views.UserCreate.as_view())
]
