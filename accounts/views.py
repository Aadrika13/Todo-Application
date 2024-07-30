from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')

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