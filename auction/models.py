from django.db import models
from authentication.models import CustomUser


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    photo = models.ImageField(upload_to='product_photo')
    min_bid_price = models.IntegerField()
    auction_end_date_time = models.DateTimeField(null=False)
    bidder = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Bid(models.Model):
    amount = models.IntegerField()
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    Bidder = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.id
