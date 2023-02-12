from rest_framework.serializers import Serializer, ModelSerializer,IntegerField

from mainapp.models import *

class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = '__all__'

class RetailerSerializer(ModelSerializer):
    class Meta:
        model = Retailer
        fields = '__all__'

class RetailerProductSerializer(Serializer):
    retailer=RetailerSerializer()
    product=ProductSerializer()
    quantity_bought=IntegerField()
    quantity_sold=IntegerField()
    def purchased_amount(self):
        return self.quantity_bought*self.product.price
    def sold_amount(self):
        return self.quantity_sold*self.product.price
    def profit(self):
        return self.sold_amount()-self.purchased_amount()
    def in_stock(self):
        return self.quantity_bought-self.quantity_sold
    def __str__(self):
        return self.retailer.name+" "+self.product.name
