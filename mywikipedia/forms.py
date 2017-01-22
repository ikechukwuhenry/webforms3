from django.db import models
from django import forms
from django.forms import ModelForm, Textarea
from mywikipedia.models import Article
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

class ArticleForm(ModelForm):
    """docstring for ."""
    class Meta:
        model = Article
        #fields = ['pub_date', 'headline', 'content', 'reporter']
        #fields = '__all__'
        exclude = ['reporter']
        widgets = {
            'content': Textarea(attrs={'cols':50, 'rows':10}),
        }
