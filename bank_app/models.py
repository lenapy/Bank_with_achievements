from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    about_user = models.TextField()
    mail_address = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    avatar = models.ImageField()
    level_points = models.IntegerField()


class Cards(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    color = models.CharField(max_length=30)


class Achievements(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    update_data = models.DateTimeField(auto_created=True)
    card = models.ForeignKey(Cards, on_delete=models.CASCADE)


class AchievementResource(models.Model):
    resource_type = models.IntegerField()
    resource_id = models.IntegerField()
    achievement = models.ForeignKey(Achievements, on_delete=models.CASCADE)
    update_data = models.DateTimeField(auto_created=True)
    resource = models.CharField(max_length=255)


class Labels(models.Model):
    text = models.CharField(max_length=30)
    color = models.CharField(max_length=20)


class UserLabels(models.Model):
    label = models.ForeignKey(Labels, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievements, on_delete=models.CASCADE)


class Observers(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    card = models.ForeignKey(Cards, on_delete=models.CASCADE)

