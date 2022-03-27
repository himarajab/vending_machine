from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='users-api'
urlpatterns = [
    path('register', views.UserCreate.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='rest_framework/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('users/', views.ListUserView.as_view(), name="users"),
    path("users/<slug:pk>/", views.DetailUserView.as_view(), name="user-update"),
    path("users/delete/<slug:pk>/", views.DestoryUserView.as_view(), name="user-delete"),
    
    path('deposit/', views.Deposit.as_view(),name="deposit"),
    path('reset/', views.Reset.as_view(),name="reset"),
    path('buy/<int:product_id>/<int:quantity>/',views.Buy.as_view(),name="buy"),
]
