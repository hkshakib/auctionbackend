from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from .views import UserRegistrationView, UserLoginView, TokenObtainView

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/login/', UserLoginView.as_view(), name='login'),
    path('api/token/', TokenObtainView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
