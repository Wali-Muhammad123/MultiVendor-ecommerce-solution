from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .models import *
from django.contrib import messages
#import django exceptions 
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
# Create your views here.
def index(request):
    products=ProductDetails.objects.all()
    context={
        'products':products
    }
    return render(request, 'index.html', context)
def register(request):
    if request.method=='POST':
        form=RetailerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainapp:login')
    else:
        form=RetailerRegistrationForm()
    context={'form':form}
    return render(request, 'register.html', context=context)
#class Login(LoginView):
    #template_name='login.html'
    #redirect_authenticated_user=True
    #form_class=LoginPageForm
    #def get_success_url(self):
        #super().__init__(self,*args,*kwargs)
        #return redirect('mainapp:retailer')
    #def form_invalid(self,form):
        #super().__init__(self,*args,**kwargs)
        #return self.render_to_response(self.get_context_data(form=form))

def loginview(request):
    if request.method=='POST':
        form=LoginPageForm(request.POST)
        if form.is_valid():
            try:
                #authenticate user
                username=request.POST.get('username')
                password=request.POST.get('password')
                user=authenticate(request,username=username,password=password)
                login(request,user)
                return redirect('mainapp:index')
            except ObjectDoesNotExist:
                loginform=LoginPageForm()
                return render(request,'login.html',context={'msg':'Invalid Credentials','form':loginform})
        else:
            loginform=LoginPageForm()
            return render(request,'login.html',context={'msg':'Add both username and password','form':loginform})
    else:
        loginform=LoginPageForm()
        return render(request,'login.html',context={'msg':'','form':loginform})

            

def logout(request):
    logout(request)
    return render(request, 'index.html')
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
        return render(request, 'retailer.html', context)
    def post(self, request):
        try:
            retailer=Retailer.objects.filter(user=request.user)
            product_name=request.POST.get('name')
            product_price=request.POST.get('price') 
            product_description=request.POST.get('product_description')
            quantity=request.POST.get('quantity')
            category=request.POST.get('category')
            if product_name and product_price and product_description and quantity and category:
                product_id=product_id(category,retailer,product_price)
                product=Product(name=product_name,product_id=product_id,price=product_price,description=product_description,category=category)
                product.save()
                retailer_product=Retailer_Product(retailer=retailer,product=product,quantity_bought=quantity)
                retailer_product.save()
                return JsonResponse({'msg':'Product added successfully'})
            
        except:
            return JsonResponse({'msg':'Error adding product'})
    def product_id(category,retailer,price):
        if category=='Electronics':
            return 'e'+str(retailer.id)+str(price)
        elif category=='Clothing':
            return 'c'+str(retailer.id)+str(price)
        elif category=='Groceries':
            return 'g'+str(retailer.id)+str(price)
        elif category=='Mobiles':
            return 'm'+str(retailer.id)+str(price)
        elif category=='Home Appliances':
            return 'ha'+str(retailer.id)+str(price)
        elif category =='Footwear':
            return 'fw'+str(retailer.id)+str(price)
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
def product(request): 
    pass


