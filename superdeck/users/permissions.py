from rest_framework import permissions


class ClientPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        permission_types = ['Client']
        return bool(request.user and request.user.user_type_humanize() in permission_types)


class BaseStaffPermission(permissions.BasePermission):
    """Technicians"""

    def has_permission(self, request, view):
        permission_types = ['Technician', 'Receptionist', 'Manager', 'Administrator']
        return bool(request.user and request.user.user_type_humanize() in permission_types)


class ReceptionistStaffPermission(permissions.BasePermission):
    """Receptionists"""

    def has_permission(self, request, view):
        permission_types = ['Receptionist', 'Manager', 'Administrator']
        return bool(request.user and request.user.user_type_humanize() in permission_types)


class StaffManagerPermission(permissions.BasePermission):
    """Can add and change """

    def has_permission(self, request, view):
        permission_types = ['Manager', 'Administrator']
        return bool(request.user and request.user.user_type_humanize() in permission_types)


class StaffAdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        permission_types = ['Administrator']
        return bool(request.user and request.user.user_type_humanize() in permission_types)
