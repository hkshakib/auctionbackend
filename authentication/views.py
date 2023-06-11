from django.contrib import auth

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import CustomTokenObtainPairSerializer, LoginSerializer, UserSerializer


class TokenObtainView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserLoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            token = CustomTokenObtainPairSerializer.get_token(user)
            return Response(data={'refresh': str(token), 'access': str(token.access_token)}, status=status.HTTP_200_OK)

        return Response({'Message': 'Email or password did not matched!'}, status=status.HTTP_401_UNAUTHORIZED)


class UserRegistrationView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            token = CustomTokenObtainPairSerializer.get_token(user)
            return Response(data={'refresh': str(token), 'access': str(token.access_token)},
                            status=status.HTTP_201_CREATED)

        return Response({'msg': "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
