from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions as pms


class IsSelfOrAdmin(pms.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user or request.user.is_admin


class IsAdminOrReadOnly(pms.BasePermission):
    def has_permission(self, request, view):
        if request.method in pms.SAFE_METHODS:
            return True
        if isinstance(request.user, AnonymousUser):
            return False
        return request.user.is_admin


class IsOwnerOrReadOnly(pms.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in pms.SAFE_METHODS:
            return True
        if isinstance(request.user, AnonymousUser):
            return False
        return request.user in obj.teachers.all() and request.user.is_owner \
                or request.user.is_admin


class IsAcademyStaff(pms.BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(request.user, AnonymousUser):
            return False
        if not request.user.is_teacher:
            return False
        return request.user.teacher in obj.teachers.all()


class IsNotAcademyStaffOrReadOnly(pms.BasePermission):
    def has_permission(self, request, view):
        if request.method in pms.SAFE_METHODS:
            return True
        if isinstance(request.user, AnonymousUser):
            return False
        return request.user.is_student or request.user.is_parent \
                or request.user.is_admin

