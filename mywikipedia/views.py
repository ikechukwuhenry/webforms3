from django.shortcuts import render, redirect, HttpResponse
from django.core import validators
from .models import Users,Article
from django.forms import Textarea
from django.forms.models import modelform_factory
from . import forms
from django.contrib.auth.decorators import login_required
from random import randint
#from .forms import UserForm
# Create your views here.
def wikipedia(request):
    users = Users.objects.all()
    randomurl = 'https://en.wikipedia.org/wiki/Special:Random'
    return render(request,'mywikipedia/wikipedia.html',{'users': users,'randomurl':randomurl})

def customLogin(request):
    form = forms.UserForm()
    if request.method == 'POST':
        print('post rewuest')
        formvalue = forms.UserForm(request.POST)

        if formvalue.is_valid():
            formvalue.clean()
            print('form is valid')
            print(formvalue.cleaned_data['username'])
            user = Users()
            user.username = formvalue.cleaned_data['username']
            user.password = formvalue.cleaned_data['password']
            user.save()
            return redirect('/wikipedia')
        #
    return render(request,'mywikipedia/wikipedia.html',{'form': form})

def modelForm(request):
    #modelform = forms.ModelForm()
    factoryform = modelform_factory(Article,fields=('headline','content'), widgets={'content':Textarea()})
    return render(request,'mywikipedia/wikipedia.html',{'form':factoryform})

def signin(request):
    form = forms.SignInForm()
    if request.method == 'POST':
        formValue = forms.SignInForm(request.POST)
        if formValue.is_valid():
            #user = Users().objects.get(formValue.cleaned_data['username'])
            user = Users.objects.all()
            usernames = []
            for currentuser in user:
                usernames.append(currentuser.username)
            if (formValue.cleaned_data['username'] in usernames) :
                print('opening a valied profile')
                return redirect('/profile')
    return render(request,'mywikipedia/signin.html', {'form': form})
#@login_required(login_url='/signin')
def profile(request):
    print('profile view called')
    articleform = forms.ArticleForm()
    return render(request, 'mywikipedia/profile.html',{'articleform': articleform})


def contact_us(request):
    form = forms.ContactForm(initial={'sender':'user@example.com'})
    return render(request, 'mywikipedia/contactus.html',{'form':form })

def login(request,template_name):
    print("login view called")
    return render(request,template_name)

def home(request):
    imageurl = "http://"
    staticurl = "/static/img/"
    ext = ".jpg"
    imageNames = ['coverpics','old-couple-kissing','sunset']
    fullurl =""
    if 'SERVER_PORT' in request.META:
        print(request.META['SERVER_PORT'])
        print(request.get_host())
        randomIndex = randint(0,(len(imageNames)-1))
        fullurl = imageurl + request.get_host() + staticurl + imageNames[randomIndex] + ext
        print(fullurl)
    return render(request,'mywikipedia/home.html')

def ajaxresponse(request):
    imageurl = "http://"
    staticurl = "/static/img/"
    ext = ".jpg"
    imageNames = ['coverpics','old-couple-kissing','sunset']
    fullurl =""
    if request.method == 'GET':
        randomIndex = randint(0,(len(imageNames)-1))
        fullurl = imageurl + request.get_host() + staticurl + imageNames[randomIndex] + ext
        #imageUrl = "http://0.0.0.0:7000/static/img/coverpics.jpg"
        return HttpResponse(fullurl, content_type="text/plain")
