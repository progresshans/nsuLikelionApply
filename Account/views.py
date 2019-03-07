from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):
    return render(request, 'Account/index.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['userPass'] == request.POST['userPassConfirm']:
            user = User.objects.create_user(request.POST['userName'], password=request.POST['userPass'])
            auth.login(request, user)
            return redirect('Home:index')
    return render(request, 'Account/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['userName']
        password = request.POST['password']
        user = auth.authenticate(request, useranme=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('')
        else:
            return render(request, 'Account/signin.html', {'error': 'username or password error'})
    else:
        return render(request, 'Account/signin.html')
        
    return render(request, 'Account/signin.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'Account/signin.html')


# Create your views here.
