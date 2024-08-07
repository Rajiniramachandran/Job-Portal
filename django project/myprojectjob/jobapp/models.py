from django.db import models
from django import forms

class UserRegistration(models.Model):
    username= models.CharField(max_length=50)
    useremail = models.EmailField(max_length=100)
    password = models.CharField(max_length=60)
    confirm_password = models.CharField(max_length=60)
    
    
    def __str__(self):
        return self.username



class UserLogIn(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=60)



    def __str__(self):
        return self.username
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=100)
    


    def __str__(self):
        return self.name
    


    
    
