from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms
from .models import Retailer

class RetailerRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2','first_name','last_name')
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
        }
    def save(self,commit=True):
        user=super(RetailerRegistrationForm,self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user
class LoginPageForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password=forms.CharField(label=("Password"),widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':'Password'}),strip=False)


class UpdateProfileForm(forms.ModelForm):
    phone=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}))
    class Meta:
        model=Retailer
        fields=('phone','address')
        widgets={
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
        }