from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccountLogin.login, name='login'),
    path('', views.Account.login, name='signup'),
]
