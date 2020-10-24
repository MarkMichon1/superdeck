from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class TestAuthenticated(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(data={"authorized": 'Success!'}, status=status.HTTP_200_OK)


class TestClientPermission(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(data={"authorized": 'Success!'}, status=status.HTTP_200_OK)


class TestBaseStaffPermission(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(data={"authorized": 'Success!'}, status=status.HTTP_200_OK)


class TestStaffReceptionistPermission(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(data={"authorized": 'Success!'}, status=status.HTTP_200_OK)


class TestStaffManagerPermission(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(data={"authorized": 'Success!'}, status=status.HTTP_200_OK)


class TestStaffAdminPermission(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(data={"authorized": 'Success!'}, status=status.HTTP_200_OK)
