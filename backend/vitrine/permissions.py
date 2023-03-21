from rest_framework import permissions
from .models import StoreFront, Services


class IsOwnerStoreFrontOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.creator == request.user


class IsOwnerServiceOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        creator_id = StoreFront.objects.get(
            id=view.kwargs['storefront_id']).creator.id
        return request.user.id == creator_id

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.store.creator == request.user
