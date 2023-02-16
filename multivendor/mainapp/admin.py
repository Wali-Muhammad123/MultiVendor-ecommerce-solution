from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from .models import * 
admin.site.register(ProductDetails)
admin.site.register(Retailer_Product)
admin.site.register(Retailer)
admin.site.unregister(User)
admin.site.register(User)
