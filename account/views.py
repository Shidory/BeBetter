from django.shortcuts import render
from django.http.response import HttpResponse
from . forms import *

# Create your views here.
class Account():
    def login(request):
        if request.method == 'POST':
            form = UserLoginForm(request.POST)
            if form.is_valid():
                form.save()
        #return render(request, 'account/login.html')
