from django.forms import ModelForm
from .models import *
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

class DonationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'type': "text",
        "class": "form-control",
        "placeholder": "Full Name"
    }),max_length=30, required=False)
    amount= forms.FloatField(widget=forms.TextInput(attrs={
        'type': "text",
        "class": "form-control",
        "placeholder": "Enter Amount"
    }), required=False)
    Email = forms.EmailField(widget=forms.TextInput(attrs={
        'type': "text",
        "class": "form-control",
        "placeholder": "Enter your Email"
    }),required=False)
    class Meta:
        model = Donation
        fields = ['name','Email','amount']