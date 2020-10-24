from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import AppUser
from users.serializers import AppUserSerializer

from users.utilities import final_validation, validate_email_return_errors, validate_password_return_errors, \
    validate_name_return_errors


class CustomUserCreate(APIView):

    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request, format='json'):
        serializer = AppUserSerializer(data=request.data)
        if serializer.is_valid():
            validation_status = final_validation(username=request.data['username'], email=request.data['email'])
            if validation_status:
                return Response(validation_status, status=status.HTTP_400_BAD_REQUEST)
            user = serializer.save()
            if user:
                return Response({}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmailValid(APIView):

    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request, format='json'):
        validation_status = validate_email_return_errors(request.data['email'])
        return Response({"email": validation_status}, status=status.HTTP_200_OK)


class PasswordValid(APIView):

    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request, format='json'):
        validation_status = validate_password_return_errors(request.data['password'])
        return Response({"password": validation_status}, status=status.HTTP_200_OK)


class LogoutAndBlacklistRefreshTokenForUserView(APIView):

    authentication_classes = ()
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)