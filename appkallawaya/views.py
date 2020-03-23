from django.shortcuts import render, redirect
from appkallawaya.forms import RegistrationForm, EditProfileForm
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


def profile(request):
    args = {'user': request.user}
    return render(request, 'kallawaya/profile.html', args)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/kallawaya/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'kallawaya/edit_profile.html', args)