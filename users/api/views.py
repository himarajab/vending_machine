from rest_framework import status
from django.db.models import F
from rest_framework import views
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from .serializers import UserSerializer,DetailUserSerializer

User=get_user_model()

class Deposit(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DetailUserSerializer
    
    
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
    permission_classes = [permissions.IsAuthenticated]
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
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DetailUserSerializer

    def delete(self, request, *args, **kwargs):
        base_response = super(DestoryUserView, self).delete(request, *args, **kwargs)
        msg = 'User deleted successfully'
        return Response(msg)


    def get_queryset(self, *args, **kwargs):
        qs = User.objects.all()
        return qs