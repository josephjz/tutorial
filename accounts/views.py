from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):  # django function based view 
    # from video 2: return HttpResponse('Home page!')   # when the user goes to the url connected to the home() function (this is a view), (look at the urls)
                                        # and you will see the path defined as views.home, respond immediately with this return 
                                        # this happeens when they load the url 

    # video 3: 
    return render(request, 'accounts/login.html') # now django will look into templates folder for HTMl
