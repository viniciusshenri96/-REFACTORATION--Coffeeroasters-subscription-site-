from django.shortcuts import render , redirect

#### login ###


def login_view(request):
    return render(request, 'pages/login/login.html')
