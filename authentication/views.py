from django.db.models import Count
from django.contrib import auth

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import CustomTokenObtainPairSerializer, LoginSerializer, UserSerializer
from .models import CustomUser

from auction.serializers import ProductSerializer
from auction.models import Product, Bid


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
                return Response(data={'refresh': str(token), 'access': str(token.access_token)},
                                status=status.HTTP_200_OK)

        return Response({'Message': 'Email or password did not matched!'}, status=status.HTTP_401_UNAUTHORIZED)


class UserRegistrationView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        print(serializer)
        print(serializer.is_valid())

        if serializer.is_valid():
            user = serializer.save()
            token = CustomTokenObtainPairSerializer.get_token(user)
            return Response(data={'refresh': str(token), 'access': str(token.access_token)},
                            status=status.HTTP_201_CREATED)

        return Response({'Message': "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)


class UserProductView(APIView):
    def get_object(self, id):
        try:
            user = CustomUser.objects.get(pk=id)
            return user
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        user = self.get_object(id)
        if user is not None:
            products = Product.objects.filter(bidder=id).all()
            product_serializer = ProductSerializer(products, many=True)
            bids = Bid.objects.all().select_related('product').filter(bidder=id)
            data = []
            for bid in bids:
                bid_data = {}
                counts = Bid.objects.all().filter(product=bid.product_id).values('product').annotate(
                    total=Count('bidder'))
                for count in counts:
                    bid_data['bid_count'] = count['total']

                bid_data['product_title'] = bid.product.title
                bid_data['biding_amount'] = bid.amount
                bid_data['starting_bid'] = bid.product.min_bid_price
                data.append(bid_data)

            context = {'products': product_serializer.data, 'bids': data}
            return Response(context, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
