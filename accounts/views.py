from django.shortcuts import render, HttpResponse, redirect
#from django.contrib.auth.forms import UserCreationForm
# now that we have our own form, we comment out above line and instead import our form 
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User 

# use default form to be able to edit the user model 
from django.contrib.auth.forms import UserChangeForm 

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

def register(request):  # video 15 

    if request.method == 'POST': # if user has filled out form 
        #form = UserCreationForm(request.POST)
        # now using our form 
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save() #creates user in db
            return redirect('/account')     # this does not handle invalid forms
    
    else:   # first time it is loaded 
        form = RegistrationForm()
    
        # pass the form through to the templates 
        args = {'form': form}

    return render(request, 'accounts/reg_form.html', args)


def view_profile(request):
    # define dictionary that we are going to pass through to this view 
    # key is what we refer to in the template, value is actual data 
    args = {'user': request.user}   # whole user object
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    # two different scenarios to account for here 
    # 1. get request to page to get page initially from server
    # 2. already has information, user has filled in info with the form to submit, and then they hit the submit button and post that data back to the webserver 
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance = request.user) # knows what data the user has entered; also pass in instance param specifies the user object 
        if form.is_valid():
            form.save()
            return redirect('/account/profile') # to see the updated information 

    else:   #accounting for the get scenario, which initializses blank form 
        form = UserChangeForm(instance = request.user)
        args = {'form': form} # data to return 
        return render(request, 'accounts/edit_profile.html', args)





