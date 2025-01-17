from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return True
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated