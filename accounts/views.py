from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):  # django function based view 
    return HttpResponse('Home page!')
