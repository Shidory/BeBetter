from django import forms
from .models import *

class UserLoginForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailField(), require=True, max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    class meta:
        model = UserModel
        fields = ['email', 'password']