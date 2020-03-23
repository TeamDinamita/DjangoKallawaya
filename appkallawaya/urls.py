from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('home/', views.home),
    path('login/', LoginView.as_view(template_name='kallawaya/login.html'))
]