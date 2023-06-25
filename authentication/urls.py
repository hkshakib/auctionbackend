from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from .views import UserRegistrationView, UserLoginView, TokenObtainView, UserProductView, UsersView, UserDetailsView

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/login/', UserLoginView.as_view(), name='login'),
    path('api/token/', TokenObtainView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/product/<int:id>/', UserProductView.as_view(), name='my_products'),
    path('api/users/', UsersView.as_view(), name='users'),
    path('api/users/<int:id>', UserDetailsView.as_view(), name='users'),

]
