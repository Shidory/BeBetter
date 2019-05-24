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
            match = UserSignUp.objects.get(username = user)
        except:
            return self.cleaned_data['username']
        raise forms.ValidationError("Username already exist!")

    def clean_email(self):
        pass