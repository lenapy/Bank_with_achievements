from bank.models import Session


class Auth:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            user_session = request.COOKIES['user-session']
            session = Session.objects.filter(token=user_session).last()
            print(session.user.login)
        except KeyError:
            pass
        response = self.get_response(request)
        return response

