from pprint import pprint
from product.models import Product
from rest_framework import status
from django.db.models import F
from rest_framework import views
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from .serializers import UserSerializer,DetailUserSerializer,BuySerializer,DepositUserSerializer
import custom_permission

User=get_user_model()

class Buy(generics.CreateAPIView):   
    serializer_class = BuySerializer        
    permission_classes = (custom_permission.IsBuyer)
    
    def get_queryset(self):
        product = Product.objects.filter(id=self.kwargs["product_id"])
        return product
    def create(self, request,product_id, quantity):
        base_request = request.data
        user_id = self.request.user.id
        serializer = self.get_serializer(data=base_request)
        product_id = self.kwargs['product_id']
        if serializer.is_valid():
            product = self.get_queryset().values(
                'id','cost','amount_available','name'
                ).first()
            order_total = quantity * product['cost']
           
            user_obj=User.objects.filter(id=user_id)
            deposit=float(user_obj.values().first()['deposit']) - float(order_total)
            pprint(deposit)
            pprint('deposit')
            user_obj.update(deposit=deposit)
            
            product['order_total'] = order_total
            response = Response(product, status=status.HTTP_201_CREATED)
        else:
            response= Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return response



    
    
class Reset(views.APIView):
    permission_classes = [custom_permission.IsBuyer]
    
    
    def post(self,request, *args, **kwargs):
        user=self.request.user
        user_obj=User.objects.filter(pk=user.id)
        user_obj.update(deposit=0)
        base_response = user_obj=User.objects.filter(pk=user.id).values('id','deposit','role').first()

        return Response(base_response)

class Deposit(generics.CreateAPIView):
    permission_classes = [custom_permission.IsBuyer]
    serializer_class = DepositUserSerializer
    
    
    def create(self,request, *args, **kwargs):
        data=request.data
        user=self.request.user
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            deposit=self.request.data['deposit']
            user_obj=User.objects.filter(pk=user.id)
            user_obj.update(deposit=F('deposit') +deposit)
            base_response = user_obj=User.objects.filter(pk=user.id).values('id','deposit','role').first()

            return Response(base_response)
        else:
            base_response= Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return base_response
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, )

class ListUserView(generics.ListAPIView):  
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DetailUserSerializer

    def get_queryset(self): 
        customer = self.request.user
        response = User.objects.all().order_by("-id")
        return response 

class DetailUserView(generics.RetrieveUpdateAPIView):
    permission_classes = [custom_permission.IsOwner]
    serializer_class = DetailUserSerializer
    # disable using of the put request as it by default will enforce update all fields 
    http_method_names = ['get','patch']

    def get_queryset(self, *args, **kwargs):
        qs = User.objects.filter(id=self.kwargs["pk"])
        return qs
    
    def patch(self,request, *args, **kwargs):
        base_response = super(DetailUserView, self).patch(request, *args, **kwargs)
        return base_response
    
    
class DestoryUserView(generics.DestroyAPIView):
    permission_classes = [custom_permission.IsOwner]
    serializer_class = DetailUserSerializer

    def delete(self, request, *args, **kwargs):
        base_response = super(DestoryUserView, self).delete(request, *args, **kwargs)
        msg = 'User deleted successfully'
        return Response(msg)


    def get_queryset(self, *args, **kwargs):
        qs = User.objects.all()
        return qs