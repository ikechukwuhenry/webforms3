from django.db import models
from django import forms


class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
