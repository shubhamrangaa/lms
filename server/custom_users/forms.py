from dataclasses import field, fields
import email
import imp
from pyexpat import model
from django import forms
from django.contrib.auth.models import User
from custom_users.models import UserProfile
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
        labels = {
            'password1': 'Password',
            'password2': 'Confirm Password',
        }

class UserProfileForm(forms.ModelForm):
    student = "student"
    user_type = [(student,"student")]
    user_role = forms.ChoiceField(required=True, choices=user_type)
    class Meta():
        model = UserProfile
        fields = ('username','email','mobile','user_role')
        labels = {
            'user_role': 'login as: '
        }
