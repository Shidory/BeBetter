from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
class Account():
    def login(request):
        return render(request, 'account/login.html')
