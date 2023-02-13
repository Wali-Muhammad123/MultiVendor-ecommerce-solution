from django.urls import path 
from . import views

urlpatterns=[
    path('',views.ProductList().as_view(),name='index'),
    path('product/<int:id>/',views.ProductDetail().as_view(),name='product_detail'),
    path('retailer_product/',views.RetailerProductList().as_view(),name='retailer_product'),
]