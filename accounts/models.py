from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save # signals allow you to execute code based on what is happening in db


# REMEMBER, everytime you change this models.py file you must makemigrations and migrate to get changes to the database 

# note: django automatically gives id for primary key of 1,2...

class UserProfile(models.Model):    # inherits tons of properties and methods from models.Model aka making it a table in django backend
    user = models.OneToOneField(User,on_delete = models.CASCADE) # link to user model that is built into django 
    # now we add our own things 

    email = models.EmailField()
    password = models.CharField(max_length=50, default = '')
    #passwordsecond = models.CharField(max_length=50,error_messages={'required': 'Please enter the same password'})#, blank=False)
    first_name = models.CharField(max_length=50, default = '')
    last_name = models.CharField(max_length=50, default = '')
    phone_number = models.IntegerField(default = 0)

    # choices
    # An iterable of values used to specify the set of valid options
    # for a field. Each value should be a tuple of two values, the first
    # being the field's value and the second being what is shown to the user.
    BIO = 'Biology'
    MGMT = 'Management'
    CS = 'Computer Science'
    MAJOR_CHOICES = (
    (BIO, 'Biology'),
    (MGMT, 'Management'),
    (CS, 'Computer Science')
    )   

    major1 = models.CharField(max_length=20,
                                choices=MAJOR_CHOICES)
    major2 = models.CharField(max_length=20,
                                choices=MAJOR_CHOICES)
                        

    courses = models.TextField(blank=True)
    housing_location = models.TextField(blank=True)
    location = models.BooleanField(default=1)
    # is_staff = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=False)


def create_profile(sender, **kwargs): 
    if kwargs['created']:        # read as if this user object has been created, then create user profile
        user_profile = UserProfile.objects.create(user=kwargs['instance']) # 

post_save.connect(create_profile, sender = User) # post_save 


