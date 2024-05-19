from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Comment

from django.shortcuts import render, redirect

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']