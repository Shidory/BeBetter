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
        pass