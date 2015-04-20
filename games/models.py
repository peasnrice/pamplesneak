from django.db import models
import datetime
from django.contrib.auth.models import User
from userprofile.models import UserProfile

class Player(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length = 64, default="")
    hosted_count = models.IntegerField(default=0)
    game_count = models.IntegerField(default=0)
    phrase_count = models.IntegerField(default=0)
    word_count = models.IntegerField(default=0)
    game_record = models.IntegerField(default=0)
    phrase_record = models.IntegerField(default=0)
    word_record = models.IntegerField(default=0)
    created_on = models.DateTimeField(editable=False)
    def __str__(self):
        return self.user.username
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id or not self.created_on:
            self.created_on = datetime.datetime.today()
        return super(Player, self).save(*args, **kwargs) 

User.player = property(lambda u: Player.objects.get_or_create(user=u)[0])

class Game(models.Model):
    players = models.ManyToManyField(Player, blank=True, null=True, related_name='games')
    host = models.ForeignKey(Player, blank=True, null=True)
    name = models.CharField(max_length=50)
    motto = models.CharField(max_length=100)
    passcode = models.CharField(max_length=16, null=True)
    created_on = models.DateTimeField(editable=False)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id or not self.created_on:
            self.created_on = datetime.datetime.today()
        return super(Game, self).save(*args, **kwargs) 

class GamePlayerDetail(models.Model):
    game = models.ForeignKey(Game, related_name = 'gpdgame')
    player = models.ForeignKey(Player, related_name = 'gpdplayer')
    score = models.IntegerField(default = 0)
    def __str__(self):
        return self.game.name

class Phrase(models.Model):
    game = models.ForeignKey(Game)
    player = models.ForeignKey(Player)
    phrase_text = models.CharField(max_length=200)
    created_on  = models.DateTimeField(editable=False)
    def __str__(self):
        return self.phrase_text   
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id or not self.created_on:
            self.created_on = datetime.datetime.today()
        return super(Phrase, self).save(*args, **kwargs)