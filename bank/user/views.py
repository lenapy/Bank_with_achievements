from django.shortcuts import render, redirect
import uuid
from django.contrib import messages


from bank.user.forms import RegistrationForm, LoginForm, PasswordChangeForm
from bank.models import User, Session


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
            session = Session.objects.create(user=form.user, token=uuid.uuid4())
            response = redirect('/')
            response.set_cookie('user-session', session.token,
                                expires=session.date_expired)
            return response
    else:
        form = LoginForm()

    return render(request, 'user/login.html', context={'form': form})


def logout(request):
    user = getattr(request, 'user', None)
    if hasattr(user, 'is_authenticated') and not user.is_authenticated:
        user = None
        request.session.flush()
    if hasattr(request, 'user'):
        from django.contrib.auth.models import AnonymousUser
        request.user = AnonymousUser()
    return render(request, 'user/logout.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST)
        if form.is_valid():
            form.save()
            session = Session.objects.update(user=form.user, token=uuid.uuid4())
            messages.success(request, 'Your password was successfully updated!')
            response = redirect('user:change_password')
            response.set_cookie('user-session', session.token,
                                expires=session.date_expired)
            return response
        else:
            messages.error(request, 'Please correct password')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/change_password.html', context={'form': form})
