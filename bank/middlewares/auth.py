from django.shortcuts import render, redirect

from bank.models import Session


class Auth:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.get_full_path() == '/user/login/':
            response = self.get_response(request)
            return response
        try:
            user_session = request.COOKIES['user-session']
            session = Session.objects.filter(token=user_session).last()
            if not session:
                return redirect('user:login')
        except KeyError:
            return redirect('user:login')
        response = self.get_response(request)
        return response

