
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout
from apply.models import Application
from apply.forms import UserApplication 
from django.urls import reverse
# Create your views here.
def home(request):
    return render(request,'apply/home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['Vpassword']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User already exists')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                return redirect('Login')
        else:
            messages.info(request,'Password mismatch')
            return redirect('signup')
    else:    
        return render(request,'apply/signup.html')

def user_login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    return render(request,'apply/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def apply(request): 
    context ={} 
  
    # create object of form 
    form = UserApplication(request.POST or None, request.FILES or None) 
      
    # check if form data is valid 
    if form.is_valid(): 
        # save the form data to model 
        form.save() 
  
    context['form']= form 
    return render(request, "apply/submit.html", context) 