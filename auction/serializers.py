from rest_framework import serializers
from .models import Product, Bid


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'min_bid_price', 'auction_end_date_time']


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ['id', 'amount', 'product', 'bidder']
