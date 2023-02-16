from django import forms 
from .models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms

class RetailerRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'})
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


