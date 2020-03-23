from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
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
            return redirect('/kallawaya/login')
        else:
            form = RegistrationForm()
            args = {'form': form}
            return render(request, 'kallawaya/register.html', args)
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'kallawaya/register.html', args)


def profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
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


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/kallawaya/profile')
        else:
            return redirect('/kallawaya/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'kallawaya/change_password.html', args)