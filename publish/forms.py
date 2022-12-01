from django import forms
from .models import Ride

class RideForm(forms.ModelForm):
    destination = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':
    'Enter your start destination', 'class': 'form-control'}))
    rideDate = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':
    'Enter ride date', 'class': 'form-control'}))

# unityid = 
# forms.CharField(required=True, 
# widget=forms.TextInput(attrs={'placeholder': 'Unity Id', 'class': 'form-control'}))

    class Meta:
        model = Ride

        fields = "__all__"
