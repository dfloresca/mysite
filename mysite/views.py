from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# imports for authentication
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth.models import  User
from django.contrib.auth import  login , logout, authenticate
from django.contrib.auth.decorators import  login_required
from django.utils.decorators import  method_decorator

def home(request):
    return render(request, "mysite/index.html")
    
def login_view(request):
    """How we login to our app"""
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active: # check the user is active
                    login(request,user)
                    return  HttpResponseRedirect(f'/user/{u}')
                else:
                    print(f'{u} - Account has been disabled')
                    return HttpResponseRedirect('/login')
            else:
                print('The username and/or password is incorrect')
                return HttpResponseRedirect('/login')
        else:
            form = AuthenticationForm()
            return render(request, 'mysite/login.html', { 'form': form })
    else:
        form = AuthenticationForm()
        return render(request, 'mysite/login.html', { 'form': form })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login")

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/polls/')
        else:
            return HttpResponseRedirect('/signup')
    else:
        form = UserCreationForm()
        return render(request, 'mysite/signup.html', { 'form': form })
