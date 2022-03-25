from django.urls import path
from . import views

app_name='product-api'
urlpatterns = [
    path('Product', views.ProductCreate.as_view()),
    
    path('products/', views.ListProductView.as_view(), name="products"),
    path("products/<slug:pk>/", views.DetailProductView.as_view(), name="product"),
    path("products/delete/<slug:pk>/", views.DestoryProductView.as_view(), name="delete_product"),
]
