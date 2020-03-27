from django.conf.urls import url
from django.urls import path, re_path

import appkallawaya
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls import handler400, handler500


urlpatterns = [
    path('', views.home),
    path('login/', LoginView.as_view(template_name='kallawaya/login.html')),
    path('logout/', LogoutView.as_view(template_name='kallawaya/logout.html')),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    url(r'^profile/(?P<pk>\d+)/', views.profile, name='user_picked'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('plants/', views.list_Plant, name='plants'),
    path('testHome/', views.testHome, name='testHome'),
    path('contact/', views.contact, name='contact'),
    path('testInit/', views.testInit, name='testInit'),
    url(r'^testInit/(?P<pk>\d+)/', views.testInit, name='testInit_picked'),
    path('herbario/', views.herbario, name='herbario'),
    url(r'^herbario/(?P<pk>\d+)/', views.herbario, name='herbario_picked'),
    path('herbario2/', views.herbario2, name='herbario2'),
    url(r'^herbario2/(?P<pk>\d+)/', views.herbario2, name='herbario2_picked')
]