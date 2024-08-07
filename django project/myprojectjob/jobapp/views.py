from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
# from django.contrib.auth import login
from .forms import UserRegisterForm
from .models import UserRegistration
from .forms import UserLogInForm
from .models import UserLogIn,ContactMessage
# from .forms import ContactForm
# from django.forms import ModelForm
from .forms import MyForm
# from .models import ContactMessage

# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import AuthenticationForm



def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    # return render(request, 'contact.html')
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MyForm()
    return render(request,'contact.html', {'form': form})

def jobs(request):
    # title = request.GET.get('title', '')
    # location = request.GET.get('location', '')
    
    # jobs = jobs.objects.all()
    
    # if title:
    #     jobs = jobs.filter(title__icontains=title)
    
    # if location:
    #     jobs = jobs.filter(location__icontains=location)
    
    # context = {
    #     'jobs': jobs,
    # }
    return render(request, 'jobs.html')

def account(request):
    return render(request, 'account.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Process the form data, save the user, etc.
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('success')  # Redirect to the success page
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def login(request):
     if request.method == "POST":
         form = UserLogInForm(request.POST)
         if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username')
             password = form.cleaned_data.get('password')
             user = authenticate(username=username, password=password)
             if user is not None:
                  auth_login(request, user)  # Correct function to log in a user
                  messages.info(request, f"You are now logged in as {username}.")
                  return redirect("home")  # Replace 'home' with your desired redirect URL
             else:
                  messages.error(request, "Invalid username or password.")
         else:
              messages.error(request, "Invalid form submission.")
     else:
         form = UserLogInForm()
     return render(request, "login.html", {"form": form})

def success(request):
    return render(request, 'success.html')


def view_contact_messages(request):
    contact_messages = ContactMessage.objects.all()
    return render(request, 'contact_messages.html', {'contact_messages': contact_messages})





