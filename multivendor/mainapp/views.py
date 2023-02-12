from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .models import *
#import django exceptions 
from django.core.exceptions import ObjectDoesNotExist
#import django csrf exempt decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    products=Product.objects.all()[:20]
    context={
        'products':products
    }
    return render(request, 'mainapp/index.html', context)
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        name=request.POST['name']
        address=request.POST['address']
        phone=request.POST['phone']
        try:
            if User.objects.filter(email=email).exists():
                return render(request, 'mainapp/register.html', context={'msg':'Email already exists'})
            if User.objects.filter(username=username).exists():
                return render(request, 'mainapp/register.html', context={'msg':'Username already exists'})
            else:
                user=User.objects.create_user(username=username, email=email, password=password)
                user.save()
                Retailer_detailes=user.retailer_set(user=user,name=name,phone=phone,address=address)
        except: 
            return render(request, 'mainapp/register.html', context={'msg':'Unknown error occured'})
        return render(request, 'mainapp/login.html')
    return render(request, 'mainapp/register.html',content_type={'msg':''})
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'mainapp/index.html')
        else:
            return render(request, 'mainapp/login.html', context={'msg':'Invalid credentials'})
    return render(request, 'mainapp/login.html', context={'msg':''})
def logout(request):
    logout(request)
    return render(request, 'mainapp/index.html')
@csrf_exempt()
def search(request):
    try:
        query=request.GET['query']
        products=Product.objects.filter(name__icontains=query)
        context={
        'products':products
         }
        return JsonResponse(context, safe=False)
    except ObjectDoesNotExist:
        return JsonResponse({'msg':'No products found'}, safe=False)
     
class RetailerView(LoginRequiredMixin,View):
    login_url='/login/'
    def get(self,request):
        retailer=Retailer.objects.filter(user=request.user)
        inventory=Retailer_Product.objects.filter(retailer=retailer)
        total_inventory=0
        total_profit=0
        for i in inventory:
            total_inventory+=i.quantity_bought
            total_profit+=i.profit()
        context={
            'retailer':retailer,
            'inventory':inventory,
            'total_inventory':total_inventory,
            'total_profit':total_profit
        }
        return render(request, 'mainapp/retailer.html', context)
    def post(self, request):
        try:
            retailer=Retailer.objects.filter(user=request.user)
            product_name=request.POST['product_name']
            product_price=request.POST['product_price'] 
            product_description=request.POST['product_description']
            quantity=request.POST['product_quantity']
            category=request.POST['category']
            product_id=product_id(category,retailer,product_price)
        except:
            pass
    def product_id(category,retailer,price):
        if category=='Electronics':
            return 'E'+str(retailer.id)+str(price)
        elif category=='Clothing':
            return 'C'+str(retailer.id)+str(price)
        elif category=='Groceries':
            return 'G'+str(retailer.id)+str(price)
        elif category=='Mobiles':
            return 'M'+str(retailer.id)+str(price)
        elif category=='Home Appliances':
            return 'HA'+str(retailer.id)+str(price)
        elif category =='Footwear':
            return 'FW'+str(retailer.id)+str(price)
        else:
            raise Exception('Invalid category')
    def put(self,request):
        try:
            retailer=Retailer.objects.filter(user=request.user)
            product_id=request.POST['product_id']
            product_name=request.POST['product_name']
            product_price=request.POST['product_price']
            product_description=request.POST['product_description']
            quantity=request.POST['product_quantity']
            category=request.POST['category']
            product=Product.objects.get(id=product_id)
            product.name=product_name
            product.price=product_price
            product.description=product_description
            product.category=category
            product.save()
            retailer_product=Retailer_Product.objects.get(product=product)
            retailer_product.quantity_bought=quantity
            retailer_product.save()
            return JsonResponse({'msg':'Product updated successfully'})
        except ObjectDoesNotExist:
            return JsonResponse({'msg':'Product does not exist'})
    def delete(self,request):
        try:
            retailer=Retailer.objects.filter(user=request.user)
            product_id=request.POST['product_id']
            product=Product.objects.get(id=product_id)
            product.delete()
            return JsonResponse({'msg':'Product deleted successfully'})
        except ObjectDoesNotExist:
            return JsonResponse({'msg':'Product does not exist'})


