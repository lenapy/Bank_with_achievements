from django.contrib import admin
from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    about_user = models.TextField(null=True, blank=True)
    mail_address = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d/')
    level_points = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'users'


class Cards(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    color = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        db_table = 'cards'


class Achievements(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    update_data = models.DateTimeField(auto_created=True)
    card = models.ForeignKey(Cards, on_delete=models.CASCADE)

    class Meta:
        db_table = 'achievements'


class AchievementResource(models.Model):
    resource_type = models.IntegerField()
    resource_id = models.IntegerField(auto_created=True)
    update_data = models.DateTimeField(auto_created=True)
    resource_files = models.FileField(upload_to='resource/%Y/%m/%d/', null=True, blank=True)
    resource_links = models.URLField(null=True, blank=True)
    achievement = models.ForeignKey(Achievements, on_delete=models.CASCADE)

    class Meta:
        db_table = 'achievement_resource'


class Labels(models.Model):
    text = models.CharField(max_length=30)
    color = models.CharField(max_length=20)

    class Meta:
        db_table = 'labels'


class UserLabels(models.Model):
    label = models.ForeignKey(Labels, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievements, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_labels'


class Observers(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    card = models.ForeignKey(Cards, on_delete=models.CASCADE)

    class Meta:
        db_table = 'observers'

admin.site.register(Users)
admin.site.register(Cards)
admin.site.register(Achievements)
admin.site.register(AchievementResource)
admin.site.register(UserLabels)
admin.site.register(Observers)
