from django.shortcuts import render, redirect
from .models import Users
from . import forms
from django.contrib.auth.decorators import login_required
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
    return render(request,'mywikipedia/wikipedia.html')

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
    return render(request, 'mywikipedia/profile.html')
