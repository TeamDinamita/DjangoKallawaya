from django.shortcuts import render, redirect
from appkallawaya.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash

# Create your views here.


def home(request):
    numbers = [1, 2, 3, 4, 5]
    name = 'MAriana Carlo'
    args = {'myName': name, 'numbers': numbers}
    return render(request, 'kallawaya/home.html', args)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/kallawaya')
        else:
            form = RegistrationForm()
            args = {'form': form}
            return render(request, 'kallawaya/register.html', args)
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'kallawaya/register.html', args)