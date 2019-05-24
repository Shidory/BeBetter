from django.db import models
#from django.contrib.auth.models import User

class UserLogin(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.email

class UserSignUp(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)