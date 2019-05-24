from django import forms
from .models import *

class UserLoginForm(forms.ModelForm):
    # email = forms.EmailField(widget=forms.EmailField())
    # password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserLogin
        fields = [
            'email',
            'password'
        ]
