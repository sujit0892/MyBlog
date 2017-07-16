import re
from django import forms
from django.contrib.auth.models import User
import os

class RegistrationForm(forms.Form):
    username=forms.CharField(label="Username")
    first=forms.CharField(label="First Name")
    last=forms.CharField(label="Last Name")
    email=forms.EmailField(label="Email")
    profilepic=forms.FileField(label="Profile Pic")
    password1=forms.CharField(label="Password",
    widget=forms.PasswordInput())
    password2=forms.CharField(label="Password Again",
    widget=forms.PasswordInput())

    def clean_username(self):
        username=self.cleaned_data["username"]
        if not re.search(r'^\w+$',username):
            raise forms.ValidationError('Username should contain only alphanumeric letter')
        try:
            username=User.objects.get(username=username)
        except:
            return username
        raise forms.ValidationError("Username alraedy taken")

    def clean_password(self):
        password1=self.cleaned_data["password1"]
        password2=self.cleaned_data["password2"]
        if password1==password2:
            return password1
        raise forms.ValidationError("password not match")


    
