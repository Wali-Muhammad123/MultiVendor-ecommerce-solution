from django.shortcuts import render
from rest_framework.views import APIView
#import response object from rest framework
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from mainapp.models import ProductDetails, Retailer_Product,Retailer
from rest_framework import generics
from django.core.exceptions import ObjectDoesNotExist
from .serializers import *
import json
import io 
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

# Create your views here.

class ProductList(generics.ListAPIView):
    queryset = ProductDetails.objects.all()
    serializer_class = ProductSerializer
    def get(self, request):
        queryset= ProductDetails.objects.all()
        serializer=ProductSerializer(queryset, many=True)
        json=JSONRenderer().render(serializer.data)
        return Response(json,status=status.HTTP_200_OK)
class ProductDetail(generics.RetrieveAPIView):
    queryset = ProductDetails.objects.all()
    serializer_class = ProductSerializer
    def get(self, request, pk):
        queryset= ProductDetails.objects.get(id=pk)
        serializer=ProductSerializer(queryset)
        json=JSONRenderer().render(serializer.data)
        return Response(json,status=status.HTTP_200_OK)
class RetailerProductList(APIView):
    queryset=Retailer_Product.objects.all()
    serializer_class=RetailerProductSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def get(self,request,pk=None):
        user=request.user
        retailer=Retailer.objects.filter(user=user).first()
        if retailer:
            try:
                queryset=Retailer_Product.objects.filter(retailer=retailer)
                serializer=RetailerProductSerializer(queryset,many=True)
                return Response(serializer.data)
            except (ObjectDoesNotExist,ValueError) as e :
                return Response(status=status.HTTP_404_NOT_FOUND,data={"message":"No products found or serializer not working properly"})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    def post(self,request,pk=None):
        user=request.user
        data=request.data
        retailer=Retailer.objects.filter(user=user).first()
        if retailer and self.data_validator(data):
            try:
                product=data['product']
                quantity_bought=data['quantity_bought']
                quantity_sold=data['quantity_sold']

                retailer_product=Retailer_Product.objects.create(retailer=retailer,product=product,quantity_bought=0,quantity_sold=0)
                serializer=RetailerProductSerializer(retailer_product)
                return Response(serializer.data)
            except (ObjectDoesNotExist,ValueError) as e :
                return Response(status=status.HTTP_404_NOT_FOUND,data={"message":"No products found or serializer not working properly"})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    def put(self,request,pk=None):
        pass 
    def data_validator(self,data):
        if all([data.get('quantity_bought'),data.get('quantity_sold'),data.get('retailer'),data.get('product')]):
            if data['quantity_bought']>=1 and data['quantity_sold']>=0:
                return True
            else:
                return False
        else:
            return False





