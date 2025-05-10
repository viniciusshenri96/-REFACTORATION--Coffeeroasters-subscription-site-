from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import usuario


# === LOGIN ===
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = usuario.objects.get(nome=username)
            if check_password(password, user.senha):
                request.session['user_id'] = user.id
                return redirect('home')
            else:
                messages.error(request, 'Usuário ou senha inválidos')
        except usuario.DoesNotExist:
            messages.error(request, 'Usuário ou senha inválidos')

    return render(request, 'pages/login/login.html')


# === CADASTRO ===
def cadastro_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('confirm_password')

        if password != password_confirm:
            messages.error(request, 'As senhas não coincidem')
            return render(request, 'pages/login/cadastro.html')

        if usuario.objects.filter(nome=username).exists():
            messages.error(request, 'Usuário já existe')
            return render(request, 'pages/login/cadastro.html')

        usuario.objects.create(nome=username, senha=make_password(password))
        messages.success(request, 'Usuário cadastrado com sucesso')
        return redirect('login')

    return render(request, 'pages/login/cadastro.html')


def home_view(request):
    return render(request, 'pages/home/home.html')