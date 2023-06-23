from rest_framework import serializers

from .models import Product, Bid, Category

from authentication.models import CustomUser


class ProductSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id',
                  'title',
                  'description',
                  'min_bid_price',
                  'auction_end_date_time',
                  'photo',
                  'bidder',
                  'email',
                  'category'
                  ]

    """
    
        Add email into response by using Custom Field
        get_email method return email using Bidder_id
        
    """

    def get_email(self, obj):
        bidder_id = obj.bidder_id
        email = CustomUser.objects.get(id=bidder_id).email
        return email


class BidSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()

    class Meta:
        model = Bid
        fields = ['id', 'amount', 'product', 'bidder', 'email', 'created_at']

    def get_email(self, obj):
        bidder_id = obj.bidder_id
        email = CustomUser.objects.get(id=bidder_id).email
        return email


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'title']
