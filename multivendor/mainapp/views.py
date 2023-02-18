from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout as auth_logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .models import *
from django.contrib import messages
#import django exceptions 
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from . import utils
# Create your views here.
def index(request):
    products=ProductDetails.objects.all()
    context={
        'products':products
    }
    return render(request, 'index.html', context)
def register(request):
    if request.method=='POST':
        registeruser=RetailerRegistrationForm(request.POST)
        registerretailer=UpdateProfileForm(request.POST)
        if registeruser.is_valid() and registerretailer.is_valid():
            form1=registeruser.save()
            form2=registerretailer.save(commit=False)
            form2.user=form1
            form2.name=form1.first_name+' '+form1.last_name
            form2.save()
            user=authenticate(username=form1.username,password=form1.password)
            login(request,user)
            return redirect('mainapp:index')
    else:
        registeruser=RetailerRegistrationForm()
        registerretailer=UpdateProfileForm()
    context={'reg1':registeruser,'reg2':registerretailer}
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
        form=LoginPageForm(request, data=request.POST)
        if form.is_valid():
            try:
                #authenticate user
                username=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password')
                user=authenticate(username=username,password=password)
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
    auth_logout(request)
    return redirect('mainapp:index')
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
        form=ProductForm()
        retailer=Retailer.objects.get_or_create(user=self.request.user)
        try:
            inventory=Retailer_Product.objects.filter(retailer__in=retailer)
        except ObjectDoesNotExist:
            inventory=None
        total_inventory=0
        total_profit=0
        if inventory:
            for i in inventory:
                total_inventory+=i.quantity_bought
                total_profit+=i.profit()
        else:
            inventory=None
        context={
            'retailer':retailer[0],
            'inventory':inventory,
            'total_inventory':total_inventory,
            'total_profit':total_profit,
            'form':form
        }
        return render(request, 'retailer.html', context)
    def post(self, request):
        form=ProductForm(request.POST)
        if form.is_valid():
            retailer=Retailer.objects.get_or_create(user=self.request.user)
            product_name=form.cleaned_data.get('name')
            product_price=form.cleaned_data.get('price')
            product_description=form.cleaned_data.get('description')
            quantity=form.cleaned_data.get('quantity')
            category=str(form.cleaned_data.get('category'))
            product_id=utils.productidgen(category, retailer[0].id, int(product_price))
            print(category)
            product=ProductDetails.objects.create(product_id=product_id,name=product_name,price=product_price,description=product_description,category=category)
            retailer_product=Retailer_Product.objects.create(product=product,retailer=retailer[0],quantity_bought=quantity)
            return redirect('mainapp:retailer')
        else:
            return JsonResponse({'msg':'Unknown error occured'}, safe=False)
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
@login_required(login_url='/login/')
def profile(request):
    if request.method=='POST':
        profileform=UpdateProfileForm(request.POST,instance=request.user)
        if profileform.is_valid():
            profileform.save()
            return redirect('mainapp:profile')
    else:
        profileform=UpdateProfileForm(instance=request.user)
    context={'form':profileform}
    return render(request, 'profile.html', context=context)
@login_required(login_url='/login/')
def report(request):
    pass 


