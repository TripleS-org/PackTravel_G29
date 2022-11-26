from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter a username', 'class': 'form-control'}))
    unityid = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Unity Id', 'class': 'form-control'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    email = forms.EmailField(required=True, max_length=60, widget=forms.EmailInput(attrs={'placeholder': 'abc@mail.com', 'class': 'form-control'}))
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': "form-control"}))
    phone_number = forms.CharField(required=True, max_length=11, widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = (
            'username',
            'unityid',
            'first_name',
            'last_name',
            'email',
            'password1',
            'phone_number',
        )

class LoginForm(forms.ModelForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your username', 'class': "form-control"}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': "form-control"}))
    class Meta:
        model = User
        fields = ('username', 'password')
