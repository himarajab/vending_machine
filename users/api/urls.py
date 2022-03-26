from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='users-api'
urlpatterns = [
    path('register', views.UserCreate.as_view()),
    path('login/', auth_views.LoginView.as_view(template_name='rest_framework/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('users/', views.ListUserView.as_view(), name="users"),
    path("users/<slug:pk>/", views.DetailUserView.as_view(), name="user"),
    path("users/delete/<slug:pk>/", views.DestoryUserView.as_view(), name="delete_user"),
    
    path('deposit/', views.Deposit.as_view()),
    path('reset/', views.Reset.as_view()),
    path('buy/<int:product_id>/<int:quantity>/',views.Buy.as_view()),
]
