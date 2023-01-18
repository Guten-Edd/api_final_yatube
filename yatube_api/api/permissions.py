from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        method_is_safe = request.method in permissions.SAFE_METHODS
        is_authenticated = request.user.is_authenticated
        return method_is_safe or is_authenticated

    def has_object_permission(self, request, view, obj):
        method_is_safe = request.method in permissions.SAFE_METHODS
        user_is_author = obj.author == request.user
        return method_is_safe or user_is_author
