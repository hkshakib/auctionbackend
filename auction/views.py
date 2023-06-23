from django.db.models import Count, Max

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import BidSerializer, ProductSerializer, CategorySerializers
from .models import Bid, Product, Category


class ProductListView(APIView):
    """
        The parser_classes attribute is set to [MultiPartParser, FormParser] to enable parsing of multipart form data
    """
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        data = []
        """
            Create a dictionary to store product data
        """
        products = Product.objects.all()
        for product in products:
            """
                for email field: Assuming 'bidder' is a ForeignKey to User model and 'email' is a field in the User model
            """
            product_data = {
                'id': product.id,
                'title': product.title,
                'category': product.category.title,
                'min_bid_price': product.min_bid_price,
                'auction_end_date_time': product.auction_end_date_time.strftime("%d-%m-%y %H:%M:%S"),
                'photo': product.photo.url if product.photo else None,
                'email': product.bidder.email,
            }

            counts = Bid.objects.all().filter(product=product.id).values('product').annotate(total=Count('bidder'))
            if counts:
                for count in counts:
                    product_data['total_bids'] = count['total']
                highest_bidder = Bid.objects.all().select_related('bidder').filter(product=product.id).first()
                product_data['highest_bidder'] = highest_bidder.bidder.email
                product_data['highest_bid'] = highest_bidder.amount
            else:
                product_data['total_bids'] = 0
                product_data['highest_bidder'] = 'None'
                product_data['highest_bid'] = product.min_bid_price

            data.append(product_data)

        return Response(data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        print(serializer)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailsView(APIView):
    def get_object(self, id):
        try:
            return Product.objects.get(pk=id)
        except Product.DoesNotExist:
            raise NotFound(detail="Product not found")

    def get(self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product)
        data = serializer.data

        highest_bidder = Bid.objects.filter(product=product).order_by('-amount').first()
        data['highest_bid'] = Bid.objects.filter(product=product).aggregate(Max('amount'))['amount__max']

        if highest_bidder:
            highest_bidder_email = highest_bidder.bidder.email
            data['highest_bidder_email'] = highest_bidder_email

        return Response(data)

    def delete(self, request, id):
        product = self.get_object(id)
        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class BidListView(APIView):

    def get(self, request):
        bid = Bid.objects.all()
        serializer = BidSerializer(bid, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        serializer = BidSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BidDetailsView(APIView):
    def get(self, request, id):
        try:
            bid = Bid.objects.get(id=id)
        except Bid.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BidSerializer(bid)
        data = serializer.data

        return Response(data)

    def delete(self, request, id):
        print(id)
        try:
            bid = Bid.objects.get(pk=id)
        except Bid.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        bid.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ParticularProductBids(APIView):
    def get(self, request, id):
        bid = Bid.objects.filter(product_id=id)

        serializer = BidSerializer(bid, many=True)
        data = serializer.data

        return Response(data)

    def delete(self, request, id):
        print(id)
        try:
            bid = Bid.objects.get(pk=id)
        except Bid.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        bid.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryListView(APIView):

    def get(self, request):

        category = Category.objects.all()
        serializer = CategorySerializers(category, many=True)
        return Response(serializer.data)
