from django.urls import path
from . import views

urlpatterns = [
    path('login', views.Account.login, name='login'),
    path('signup', views.Account.signup, name='signup'),
]
