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
      request_user_id  =int(request.parser_context['kwargs']['pk'])
      product = Product.objects.get(id=request_user_id)
      seller_id = product.seller.id
      return user_id == seller_id