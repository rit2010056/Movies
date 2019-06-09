from rest_framework import permissions

class Authenticated(permissions.BasePermission):
    """
    Custom permission to only to superuser of an object to edit it.
    """

    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if request.method == 'GET':
            return True
        else:
            print(request.user.is_staff,request.user)
            return bool(request.user and request.user.is_staff)
