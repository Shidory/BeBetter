from django.urls import path
from . import views

urlpatterns = [
    path('', views.Account.login, name = 'login'),
]
