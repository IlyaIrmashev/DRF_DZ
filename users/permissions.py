from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator(BasePermission):
    info = 'Не модератор!'

    def has_permission(self, request, view):
        if request.user.role == UserRoles.moderator:
            return True
        return False


class IsBuyer(BasePermission):
    info = 'Не владелец!'

    def has_object_permission(self, request, view, obj):
        return obj.buyer == request.user or request.user.is_superuser
