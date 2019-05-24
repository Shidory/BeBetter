from django import forms
from .models import *

class UserLoginForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailField(), max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, max_length=32)

    class Meta:
        model = UserLogin
        fields = ['email', 'password']
