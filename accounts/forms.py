# creating django form for the register page 

from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm


# extending UserCreationForm to our customized one  # NOTE FOR BIBLIO: look into UserCreationForm function documentation and maybe rewrite it 

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User    # model that it is linked to 
        fields = {  # need these fields to be the fields we want from this django form 
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        }
    
    def save(self, commit = True): # ALLOWS THE FORM TO SAVE THE DATA TO THE MODEL 
        user = super(RegistrationForm, self).save(commit = False) # this switch to false says wait we need a few more fields for the model
        # we already have username, password1, and password2 going in, but not the other three that we have in our model, but not our form 
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:   # if we want to save, store that data with the next line 
            user.save()

        return user





