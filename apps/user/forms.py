from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']

        widgets = {
            "username": forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'Valid Email ID'}),
            "first_name": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'First Name','pattern':'[A_Za-z]+','title':'Enter Characters Only '}),
            "last_name": forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Last Name','pattern':'[A_Za-z]+','title':'Enter Characters Only '}),
            "password": forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'create password'})
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Valid Email ID'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': ' Password'}))
