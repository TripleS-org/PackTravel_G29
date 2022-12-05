"""Django forms for ride creation functionality"""
from django import forms
from .models import Ride

class RideForm(forms.ModelForm):
    source = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Enter your starting point here", "class": "form-control"}))
    destination = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Enter your destination here", "class": "form-control"}))

    class Meta:
        model = Ride
        fields = "__all__"
