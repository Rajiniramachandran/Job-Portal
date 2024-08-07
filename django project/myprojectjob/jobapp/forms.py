from django import forms
from jobapp.models import UserRegistration
from jobapp.models import UserLogIn
from jobapp.models import ContactMessage
from django.forms import ModelForm
# from jobapp.forms import UserRegisterForm
# from jobapp.forms import UserLogInForm






class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="UserName")
    useremail = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label="UserEmail")
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Password")
    confirm_password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Confirm Password")

    def __str__(self):
        return self.username
    

    class Meta:
        model = UserRegistration
        fields =['username','useremail','password','confirm_password']


class UserLogInForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="UserName")
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Password")


    def __str__(self):
        return self.username
    

    class Meta:
        model = UserLogIn
        fields = '__all__'


class MyForm(forms.ModelForm):
    class Meta:
        # pass
        model=ContactMessage
        fields=['name','email','message',]


   


    
