from django.core import validators
from django import forms
from .models import User
from .models import Userlogin

class StudentRegistration(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','mobile','sex','document']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'mobile':forms.TextInput(attrs={'class':'form-control'}),
            'sex': forms.Select(choices=User.SEX_CHOICES),
            'document': forms.ClearableFileInput(attrs={'class': 'form-control'}),  # Update here
        }

class AnotherForm(forms.ModelForm):
    class Meta:
        model=Userlogin
        fields=['email','password']
        widgets={
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }
