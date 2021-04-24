#from django.conf.urls import url
from django.urls import path, include 
from . import views 

from django.contrib.auth.views import LoginView # 

urlpatterns = [
    path('', views.home),
    # path('login/', LoginView, {'template_name':'accounts/login.html'}) # since we are in the accounts app, this will be at accounts/login 
                                # since we imported this build in view, it is not a function based view that we write like the home function above
                                # third param specifies which template to render since we don't have this info from the views._ function
                                # key template name tells that the value should be rendered instead of the default 
    path("login/", LoginView.as_view(template_name='accounts/login.html')) # lots of depreciated code from the tutorial 

]