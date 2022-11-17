from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    """
    For accessing the inbuilt User model
    """
    username = forms.EmailField(required=True,label="Please enter your email address",widget=forms.EmailInput(attrs={"class": "form-control"}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']

        widgets = {
            #"username": forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'Valid Email ID'}),
            "first_name": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'First Name','pattern':'[A-Z a-z]+','title':'Enter Characters Only '}),
            "last_name": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Last Name','pattern':'[A-Z a-z]+','title':'Enter Characters Only '}),
            "password": forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'create password'})
        }


class LoginForm(forms.Form):
    """
    2 Fields for loggin in.No connection with any model.
    """
    #username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Valid Email ID'}))
    username = forms.EmailField(required=True,label="Please enter your email address",widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': ' Password'}))
