# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from myblog.form import *
from django.http import HttpResponseRedirect
from .models import *
import os

# Create your views here.
def main_page(request):
    return render(request,"myblog/main_page.html")

def register_page(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            user=User.objects.create_user(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first'],
                last_name=form.cleaned_data['last'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            f=request.FILES['profilepic']
            with open('myblog/static/'+f.name, 'wb+') as destination:
                 for chunk in f.chunks():
                     destination.write(chunk)
           
            mybloguser=MyBlogUser.objects.create(user=user,profilepic=f)
            return HttpResponseRedirect("/")
    else:
        form=RegistrationForm()
    return render(request,"registration/register.html",{"form":form})

