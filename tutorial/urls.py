"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include 
from tutorial import views

urlpatterns = [
    path('',views.login_redirect, name = 'login_redirect'),  # so that first page takes you to login  OOOO THIS IS SWEET 
    path('admin/', admin.site.urls),
    path('account/', include('accounts.urls')), # tells code to "include" the accounts.urls.py file in the accounts app of this project 
                                                # note that we are currently in the wider tutorial project 
]
