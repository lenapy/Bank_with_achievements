from django.db import models
from django.contrib.auth.hashers import make_password


class UserManager(models.Manager):

    def registration(self, login, password):  # self - model
        password_hash = make_password(password, hasher='md5')
        user = self.create(login=login, password=password_hash)
        user.save()
        return user.pk

