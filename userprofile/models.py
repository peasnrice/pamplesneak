from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    games_played_count = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username

class Nickname(models.Model):
    userprofile = models.ForeignKey(UserProfile)
    nickname_text = models.CharField(max_length=32)
    def __str__(self):
        return self.nickname_text

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
