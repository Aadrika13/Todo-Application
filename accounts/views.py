from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages                                                                                                              # methods in auth model: authenticate() ,login() ,logout()
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            if user.is_staff:
                auth.login(request, user)  # session create ho rha h
                return redirect('index')
            
            else:
                auth.login(request, user)
                return redirect('todo')
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')

    return render(request, 'accounts/login.html')

#==================================== REGISTER =======================================================================================

def register(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        new_user = User(
            username = username
        )

        new_user.set_password(password)

        new_user.save()

        return redirect('login')
    
    return render(request, "accounts/register.html")

#==================================== LOGOUT ==========================================================================================

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('home')