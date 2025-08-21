from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """Проверка принадлежности пользователя к группе модераторов."""

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Moderators').exists()


class IsOwner(permissions.BasePermission):
    """Проверка принадлежности пользователя к владельцам объекта."""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False