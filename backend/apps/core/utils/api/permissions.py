from rest_framework import permissions


class IsAdminOrIsRelatedUserObject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsAdminOrSelfObject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        return obj == request.user


class IsAdminOrSelf(permissions.BasePermission):
    """Allow unsafe methods for admin users only."""

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated():
            return False
        if request.user.is_superuser:
            return True
        if request.method in permissions.SAFE_METHODS:
            return bool(Group.objects.get(name='Patient').
                        user_set.filter(id=request.user.id).exists())
        return False
