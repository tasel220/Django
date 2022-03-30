from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'],
            password=request.POST['password1'])
            auth.login(request, user)
            return redirect('/posts')
    return render(request, 'accounts/signup.html') 

def login(request):
    if request.method == 'POST':
        # user = auth.get_user(request)
        user = User.objects.get(username=request.POST['username'])
        auth.login(request, user)
        
        # user = auth.get_user(request)
        # auth.login(request, user)
        if auth.user_logged_in:
            return redirect('/posts')

        if auth.user_login_failed:
            return render(request, 'accounts/failed.html')
    return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/posts')

def failed(request):
    return render(request, 'accounts/failed.html')