from django import forms
from .models import *

class UserLoginForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)

    class Meta:
        model = UserLogin
        fields = [
            'email',
            'password'
        ]

class UserSignUpForm(forms.ModelForm):
    pass