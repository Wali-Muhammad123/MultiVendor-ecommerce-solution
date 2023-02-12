from django.contrib import admin

# Register your models here.
from .models import * 
admin.site.register(ProductDetails)
admin.site.register(Retailer_Product)
admin.site.register(Retailer)
admin.site.register(User)
