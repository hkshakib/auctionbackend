from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

        def create(self, validate_data):
            return CustomUser.objects.create_user(**validate_data)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ['email', 'password']


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # token['email]'] = user.email

        return token
