from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    class Meta : 
        model = Contact                                     # Table name
        fields = ('subject', 'email', 'sender', 'detail')   # Column name
        widgets = {
            'subject': forms.TextInput(attrs={
                'class': 'form-control col-xl-8'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control col-xl-8'
            }),
            'sender': forms.TextInput(attrs={
                'class': 'form-control col-xl-8'
            }),
            'detail': forms.Textarea(attrs={
                'class': 'form-control col-xl-8'
            })
        }

class RegisterForm(UserCreationForm):
    email= forms.EmailField()
    class Meta:
        model= User
        fields= ['username', 'email', 'password1', 'password2']
