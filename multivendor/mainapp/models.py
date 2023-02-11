from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser,BaseUserManager
from django.db.models.signals import post_save,pre_save,pre_delete
from django.dispatch import receiver
# Create your models here.
#create a User model with email as the username
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email',max_length=60,unique=True)
    username = models.CharField(max_length=30,unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True
class Retailer(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class ProductDetails(models.Model):
    CATEGORY_CHOICES=(
        ('Electronics','Electronics'),
        ('Clothing','Clothing'),
        ('Footwear','Footwear'),
        ('Home Appliances','Home Appliances'),
        ('Mobiles','Mobiles')
        ('Groceries','Groceries')
    )
    id=models.AutoField(primary_key=True)
    category=models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    name=models.CharField(max_length=30)
    product_id=models.CharField(max_length=30)
    price=models.FloatField()
    description=models.CharField(max_length=200)
#Many_to_many relation between ProductDetails and Retailer
class Retailer_Product(models.Model):
    id=models.AutoField(primary_key=True)
    retailer=models.ForeignKey(Retailer,on_delete=models.CASCADE)
    product=models.ForeignKey(ProductDetails,on_delete=models.CASCADE)
    quantity_bought=models.IntegerField(default=0)
    quantity_sold=models.IntegerField(default=0)
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
    def save(self,*args,**kwargs):
        #add validation for quantity_bought and quantity_sold
        if self.quantity_sold>self.quantity_bought:
            raise ValueError("Quantity sold cannot be greater than quantity bought")
        elif self.quantity_sold<0 or self.quantity_bought<=0:
            raise ValueError("Quantity bought cannot be negative or zero. Should be at least one.")
        else:
            super().save(*args,**kwargs)
    