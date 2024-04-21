from rest_framework import permissions

class IsAdminOrSelf(permissions.BasePermission):
    """
    Allow access only to admin user or ressource ownership
    """
    def has_object_permission(self, request, view, obj):
        # Check if the user's ID matches the object's ID
        return request.user.is_staff or request.user == obj