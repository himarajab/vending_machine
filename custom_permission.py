from rest_framework import permissions
from users.models import User
from pprint import pprint


class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
      user_id = request.user.id
      request_user_id  =int(request.parser_context['kwargs']['pk'])
      return user_id == request_user_id