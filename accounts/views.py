from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):  # django function based view 
    # from video 2: return HttpResponse('Home page!')   # when the user goes to the url connected to the home() function (this is a view), (look at the urls)
                                        # and you will see the path defined as views.home, respond immediately with this return 
                                        # this happeens when they load the url 

    # video 3: 
    # return render(request, 'accounts/login.html') # now django will look into templates folder for HTMl

    # video 6:
    # in the views, we pass data from views to our template, so this is where the logic is 
    # this is where we write our data base queries 
    numbers = [1,2,3,4,5]
    name = 'Jennifer Joseph'

    # we pass the data with the render function, with the dictionary object parameter
    args = {
        'name' : name,  #key name, we call it whatever we want, this is how we refer to this data in the HTML template itself 
        'numbers': numbers,
    }

    return render(request, 'accounts/home.html',args) 

