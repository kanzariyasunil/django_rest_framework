from rest_framework.permissions import BasePermission

class MyPermissions(BasePermission):
    def has_permission(self, request, view):
        # if request.method == 'GET': if you try to get the data it denine the permission 
        if request.method == 'POST': # it only give post method to access, all other method are not permit in costome permission.
            return True
        return False