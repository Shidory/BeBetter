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
    first_name = forms.CharField()
    last_name = forms.CharField()
    user_name = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()
    password_conf = forms.CharField()

    class Meta:
        model = UserSignUp
        fields = [
            'first_name',
            'last_name',
            'user_name',
            'email',
            'password',
            'password_conf'
        ]