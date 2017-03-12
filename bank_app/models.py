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


class AchievementResources(models.Model):
    resource_type = models.IntegerField()
    update_data = models.DateTimeField(auto_created=True)
    achievement = models.ForeignKey(Achievements, on_delete=models.CASCADE)

    class Meta:
        db_table = 'achievement_resources'


class Links(models.Model):
    link = models.URLField()
    achievement_resource = models.ForeignKey(AchievementResources, on_delete=models.CASCADE)

    class Meta:
        db_table = 'links'


class Files(models.Model):
    file = models.FileField(upload_to='resource/%Y/%m/%d/')
    achievement_resource = models.ForeignKey(AchievementResources, on_delete=models.CASCADE)

    class Meta:
        db_table = 'files'


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
admin.site.register(AchievementResources)
admin.site.register(UserLabels)
admin.site.register(Observers)
