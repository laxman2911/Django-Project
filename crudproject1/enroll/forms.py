from django.core import validators
from django import forms
from .models import User
from .models import Userlogin

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','mobile','document']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'mobile':forms.TextInput(attrs={'class':'form-control'}),
            'document': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class AnotherForm(forms.ModelForm):
    class Meta:
        model=Userlogin
        fields=['email','password']
        widgets={
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }
