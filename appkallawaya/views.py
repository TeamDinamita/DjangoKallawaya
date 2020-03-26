from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from appkallawaya.forms import RegistrationForm, EditProfileForm, HomeFormInit
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import Plant, Plant2, MalestaresTable
from django.views.generic import TemplateView
from appkallawaya.models import Post

from urllib.parse import quote

from django.template import Context, Engine, loader
from django.views.defaults import page_not_found

ERROR_404_TEMPLATE_NAME = 'kallawaya/error404.html'
ERROR_500_TEMPLATE_NAME = 'kallawaya/error500.html'


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
    if request.user.is_authenticated:
        if pk:
            user = User.objects.get(pk=pk)
        else:
            user = request.user
        args = {'user': user}
        return render(request, 'kallawaya/profile.html', args)
    else:
        return render(request, 'kallawaya/error404.html')


def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('/kallawaya/profile')
        else:
            form = EditProfileForm(instance=request.user)
            args = {'form': form}
            return render(request, 'kallawaya/edit_profile.html', args)
    else:
        return render(request, 'kallawaya/error404.html')


def change_password(request):
    if request.user.is_authenticated:
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
    else:
        return render(request, 'kallawaya/error404.html')


def list_Plant(request):
    queryset = Plant.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "kallawaya/plants.html", context)


def testHome(request):
    return render(request, 'kallawaya/testHome.html')


def contact(request):
    return render(request, 'kallawaya/contact.html')


def testInit(request):
    return render(request, 'kallawaya/testInit.html')


def herbario(request, pk=None):
    if pk == None:
        plants = Plant.objects.all()
        users = User.objects.all()
        return render(request, 'kallawaya/herbario.html', {'plants': plants})
    else:
        if pk:
            plant = Plant.objects.get(pk=pk)
        else:
            plant = request.plant
        args = {'plant': plant}
        return render(request, 'kallawaya/infoPlant.html', args)


class HomeView(TemplateView):
    template_name = 'kallawaya/testInit.html'

    def get(self, request):
        form = HomeFormInit()
        return render(request, self.template_name, {'form': form})


def herbario2(request, pk=None):
    if pk == None:
        plants = Plant2.objects.all()
        return render(request, 'kallawaya/herbario2.html', {'plants': plants})
    else:
        if pk:
            plant = Plant2.objects.get(pk=pk)
        else:
            plant = request.plant
        args = {'plant2': plant}
        return render(request, 'kallawaya/infoPlant2.html', args)