from rest_framework import permissions


class IsUserOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (obj == request.user) | request.user.is_staff













