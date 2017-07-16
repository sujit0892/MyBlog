# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    auther=models.ForeignKey(User)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class MyBlogUser(models.Model):
    user=models.ForeignKey(User)
    profilepic=models.FileField()
