
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import permissions
from .serializers import DetailProductSerializer,ProductSerializer
from ..models import Product
import custom_permission
class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated, )

class ListProductView(generics.ListAPIView):  
    permission_classes = [permissions.AllowAny]
    serializer_class = DetailProductSerializer

    def get_queryset(self): 
        response = Product.objects.all().order_by("-id")
        return response 

class DetailProductView(generics.RetrieveUpdateAPIView):
    permission_classes = [custom_permission.IsProductOwner]
    serializer_class = DetailProductSerializer
    http_method_names = ['patch','get']

    def get_queryset(self, *args, **kwargs):
        qs = Product.objects.filter(id=self.kwargs["pk"])
        return qs
    
    def patch(self,request, *args, **kwargs):
        base_response = super(DetailProductView, self).patch(request, *args, **kwargs)
        return base_response
    
    
class DestoryProductView(generics.DestroyAPIView):
    permission_classes = [custom_permission.IsProductOwner]
    serializer_class = DetailProductSerializer

    def delete(self, request, *args, **kwargs):
        base_response = super(DestoryProductView, self).delete(request, *args, **kwargs)
        msg = 'Product deleted successfully'
        return Response(msg)


    def get_queryset(self, *args, **kwargs):
        qs = Product.objects.all()
        return qs