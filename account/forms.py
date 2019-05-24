from django import forms
from .models import *

class UserLoginForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailField(), require=True, max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, require=True, max_length=32)

    class Meta:
        model = UserLogin
        fields = ['email', 'password']
