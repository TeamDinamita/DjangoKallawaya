from django.shortcuts import render

# Create your views here.


def home(request):
    numbers = [1, 2, 3, 4, 5]
    name = 'MAriana Carlo'
    args = {'myName': name, 'numbers': numbers}
    return render(request, 'kallawaya/login.html', args)