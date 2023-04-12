from rest_framework import permissions


class IsAccountOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_superuser
            and request.user.is_authenticated
            or obj.user == request.user
        )
