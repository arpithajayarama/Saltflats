from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.db import models


class RegistrationForm(UserCreationForm):
    email= forms.EmailField(required= True)

    class Meta:
       model = User
       fields = (
         'username',
         'first_name',
         'last_name',
         'email',
         'password1',
         'password2'
        )

    def save(self, comit=True):
       user = super(RegistrationForm,self).saved(commit=False)
       user.first_name= self.cleaned_data['first_name']
       user.last_name= self.cleaned_data['lasr_name']
       user.email= selfself.cleaned_data['email']

       if commit:
           user.save()

       return user

class EditProfileForm(UserChangeForm):
    class Meta:
        model= User
        fields =(
         'first_name',
         'last_name',
         'email',
         'password'
        )
