from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home),
    path('login/', LoginView.as_view(template_name='kallawaya/login.html')),
    path('logout/', LogoutView.as_view(template_name='kallawaya/logout.html')),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('plants/', views.list_Plant, name='plants'),
    path('testHome/', views.testHome, name='testHome'),
<<<<<<< HEAD
    path('testInit/', views.testInit, name='testInit'),
    path('contact/', views.contact, name='contact')

=======
    path('testInit/', views.testInit, name='testInit')
>>>>>>> 2bd23047690e08f52494792f403a5fe426ad8883
]