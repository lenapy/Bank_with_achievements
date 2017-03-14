from django.conf.urls import url

from bank.user import views

urlpatterns = [

    url(r'^registration/$', views.registration, name='registration'),
    url(r'^login/$', views.login, name='login'),
    url(r'^success_registration/$', views.success_registration, name='success_registration'),

]