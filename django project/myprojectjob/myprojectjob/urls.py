"""
URL configuration for myprojectjob project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jobapp.views import index
from jobapp.views import about 
from jobapp.views import contact
from jobapp.views import jobs
from jobapp.views import account
from jobapp.views import register
from jobapp.views import login
from jobapp.views import success
from jobapp.views import  view_contact_messages


# from jobapp.views import register
# from jobapp.views import profile



urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('index/about', about, name='about'),
    path('index/contact', contact, name='contact'),
    path('index/jobs/', jobs, name='jobs'),
    path('index/account', account, name='account'),
    path('index/register', register, name='register'),
    path('index/login', login, name='login'),
    path('index/success', success, name='success'),
    # path('index/view_contact_messages', view_contact_messages, name='view_contact_messages'),
   

#     path('about/', views.about, name='about'),
#     path('jobs/', views.jobs, name='jobs'),com
#     path('contact/', views.contact, name='contact'),
#     path('register/', views.register, name='register'),
#     path('post-job/', views.post_job, name='post_job'),
#     path('filter-search/', views.filter_search, name='filter_search'),
#     path('account/', views.account, name='account'),
#     path('login/', views.login, name='login'),
#     path('dashboard/', views.dashboard, name='dashboard'),
#
]
