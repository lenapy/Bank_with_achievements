from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from bank import models



def index(request):
    achievements = models.Achievement.objects.all()
    return render(request, 'index.html', {'achievements': achievements})
