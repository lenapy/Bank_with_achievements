from django.shortcuts import render, redirect

from bank.user.forms import RegistrationForm, LoginForm
from bank.models import User


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            if not User.objects.registration(
                form.cleaned_data['login'],
                form.cleaned_data['password']
            ):
                pass
            return redirect('user:success_registration')
    else:
        form = RegistrationForm()
    return render(request, 'user/registration.html',
                  context={'form': form})


def success_registration(request):
    return render(request, 'user/success_registration.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'user/login.html',
                  context={'form': form})
