from rest_framework import permissions
from users.models import User
from pprint import pprint
from product.models import Product

class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
      user_id = request.user.id
      request_user_id  =int(request.parser_context['kwargs']['pk'])
      return user_id == request_user_id
    
class IsProductOwner(permissions.BasePermission):
    def has_permission(self, request, view):
      user_id = request.user.id
      product_id  =int(request.parser_context['kwargs']['pk'])
      product_object = Product.objects.filter(seller_id=user_id,id=product_id)
      if product_object.exists():
        seller_id = product_object.values('seller_id').first()['seller_id']
        return user_id == seller_id
      else:
        return False

class IsBuyer(permissions.BasePermission):
    def has_permission(self, request, view):
      user_id = request.user.id
      user_role = User.objects.filter(id=user_id).values('role').first()['role']
      
      return user_role == 'buyer'
