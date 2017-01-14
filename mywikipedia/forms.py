from django.db import models
from django import forms


class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    confirm_password = forms.CharField()
class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
