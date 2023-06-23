from django.urls import path
from .views import ProductListView, ProductDetailsView, BidListView, ParticularProductBids, CategoryListView

urlpatterns = [

    path('api/products/', ProductListView.as_view(), name='product'),
    path('api/category/', CategoryListView.as_view(), name='category'),
    path('api/products/<id>/', ProductDetailsView.as_view(), name='product_details'),

    path('api/bid/', BidListView.as_view(), name='bid'),
    path('api/bid/<int:id>/', ParticularProductBids.as_view(), name='product_bids'),
    # path('api/bid/<id>/', BidDetailsView.as_view(), name='bid_details'),
]
