from django.shortcuts import render
from .models import *
from .forms import *
from django.http import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse

class Account:
    def login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            try:
                user = auth.authentifacte(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    return render(request, 'home.html')
                else:
                    messages.error(request, 'Username and password did not matched!')
            except auth.ObjectNotExist():
                print("Invalid user")
        return render(request, 'account/login.html')

    def signup(request):
        if request.method == 'POST':
            form = UserSignUpForm(request.POST)
            if form.is_valid():
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                messages.success(request, 'User registration successful')
                usr = auth.authentifacte(username=username, password=password)
                auth.login(request, usr)
                return render(request, 'account/login')
        else:
            form = UserSignUpForm()
        return render(request, 'account/registration.html', {'frm': form})