from django.urls import path

from administrative.api_views import TestAuthenticated, TestBaseStaffPermission, TestClientPermission, \
    TestStaffAdminPermission, TestStaffManagerPermission, TestStaffReceptionistPermission

urlpatterns = [
    path('test/authenticated/', TestAuthenticated.as_view(), name="administrative-test-authenticated"),
    path('test/permission/client/', TestClientPermission.as_view(), name="administrative-test-client-permission"),
    path('test/permission/staff/base/', TestBaseStaffPermission.as_view(), name="administrative-test-base-staff-permission"),
    path('test/permission/staff/receptionist/', TestStaffReceptionistPermission.as_view(), name="administrative-test-staff-receptionist-permission"),
    path('test/permission/staff/manager/', TestStaffManagerPermission.as_view(), name="administrative-test-staff-manager-permission"),
    path('test/permission/staff/admin/', TestStaffAdminPermission.as_view(), name="administrative-test-staff-admin-permission"),

]
