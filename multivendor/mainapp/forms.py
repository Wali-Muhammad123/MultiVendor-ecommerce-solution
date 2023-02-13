from django import forms 
from .models import User
from django.contrib.auth.forms import UserCreationForm 
from .models import User
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms


class RetailerRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','firstname','lastname','email','password1','password2']
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'firstname':forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'lastname':forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'})
        }
class LoginPageForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password=forms.CharField(label=("Password"),widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':'Password'}),strip=False)


