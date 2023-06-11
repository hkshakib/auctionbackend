from django.urls import path
from .views import *

urlpatterns=[
    path('api/products/', ProductListView.as_view(), name='product'),
    path('api/products/<id>/', ProductDetailsView.as_view(), name='product_details'),
    path('api/bid/', BidListView.as_view(), name='bid'),
    path('api/bid/<id>/', BidDetailsView.as_view(), name='bid_details'),
]