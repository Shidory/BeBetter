from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.validators import validate_email

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
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'First name'}
    ), required=True, max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last name'}
    ), required=True, max_length=50)
    user_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}
    ), required=True, max_length=50)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'E-mail'}
    ), required=True, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}
    ), required=True, max_length=50)
    password_conf = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password confirm'}
    ))

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

    def clean_username(self):
        user = self.cleaned_data['username']
        try:
            match = UserSignUp.objects.get(username=user)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError("Username already exist!")

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            mail = validate_email(email)
        except:
            return forms.ValidationError("Email is not in correct format")

    def clean_password_conf(self):
        pwd = self.cleaned_data['password']
        pwd_conf = self.cleaned_data['password_conf']
        min_lenght = 8
        if pwd and pwd_conf:
            if pwd != pwd_conf:
                raise forms.ValidationError("Password and password confirm not matched!")
            else:
                if len(pwd) <min_lenght:
                    raise forms.ValidationError("Password should have atleast %d characters!" %min_lenght)
                if pwd.isdigit():
                    raise forms.ValidationError("Password should not all numeric")
