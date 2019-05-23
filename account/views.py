from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
"""class Account():
    def login(self, request):
        return render(request, 'account/login.html')"""
def login(request):
    return render(request, 'account/login.html')