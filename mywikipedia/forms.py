from django.db import models
from django import forms

TOP_CHOICES = (
    ('general', 'General enquiry'),
    ('bug', 'Bug report'),
    ('suggestion', 'Suggestion'),
    )

class UserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean(self):
        if (self.cleaned_data.get('password')) != (self.cleaned_data.get('confirm_password')):
            raise forms.ValidationError("password must match")
        return self.cleaned_data

class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=TOP_CHOICES)
    message = forms.CharField(widget=forms.Textarea(),initial="replace with your feedback")
    sender = forms.EmailField(required=False)
