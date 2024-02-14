from django.shortcuts import render

# imports for authentication
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth.models import  User
from django.contrib.auth import  login , logout, authenticate
from django.contrib.auth.decorators import  login_required
from django.utils.decorators import  method_decorator

def home(request):
    return render(request, "mysite/index.html")
    
def login(request):
    """How we login to our app"""