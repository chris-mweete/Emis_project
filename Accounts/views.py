from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.contrib.auth.models import User




def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
       # Get form values
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       username = request.POST['username']
       email = request.POST['email']
       password = request.POST['password']
       password2 = request.POST['password2']
       
       #Check if password match
       if password == password2:
        if User.objects.filter(username=username).exists():
            messages.error(request,'That username is taken')
            return redirect('register')
        else:
             if User.objects.filter(email=email).exists():
                messages.error(request,'That email is taken')
                return redirect('register')
             else:
                 user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name) 
                 
                # auth.login(request, user) 
                 #messages.success(request, 'You are now loged in')
                 #return redirect('index')
                 user.save()
        messages.success(request, 'You are now registered and can login')
        return redirect('login')
       else:
            messages.error(request,'password do not match')
            return redirect('register')
            
    else:
        return render(request, 'profile/register.html')

def login(request):
    if request.method == 'POST':
        print("post request received")
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate( username=username, password=password)
        
        print ("authenticating user")
        if user is not None:
            auth.login(request, user)
            
            print("login successfull")
            return redirect('dashboard')
        else:
            print(" login failed")
            return redirect('login')
    else:
             return render(request, 'profile/login.html')

@login_required(login_url='/login')        
def dashboard(request):
    return render(request, 'profile/dashboard.html')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
