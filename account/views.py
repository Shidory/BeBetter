from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import *
from .forms import *
from .models import *

class Account:
    def login(request):
        if request.method == 'POST':
            form = UserLoginForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/account/')
        else:
            form = UserLoginForm()
        return render(request, 'account/login.html', {'form':form})

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
        return render(request, 'registration.html', {'frm': form})