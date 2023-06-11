from rest_framework import serializers

from .models import Product, Bid

from authentication.models import CustomUser


class ProductSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'min_bid_price', 'auction_end_date_time', 'photo', 'bidder', 'email']

    """
    
        Add email into response by using Custom Field
        get_email method return email using Bidder_id
        
    """
    def get_email(self, obj):
        bidder_id = obj.bidder_id
        email = CustomUser.objects.get(id=bidder_id).email
        return email


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ['id', 'amount', 'product', 'bidder']
