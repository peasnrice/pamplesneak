from django.db import models
import datetime
from django.contrib.auth.models import User
from userprofile.models import UserProfile


class Game(models.Model):
    name = models.CharField(max_length=50)
    motto = models.CharField(max_length=100)
    created_on = models.DateTimeField(editable=False)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id or not self.created_on:
            self.created_on = datetime.datetime.today()
        return super(Game, self).save(*args, **kwargs) 

class Player(models.Model):
    game = models.ForeignKey(Game)
    nickname = models.CharField(max_length=64)
    user = models.ForeignKey(User)
    created_on = models.DateTimeField(editable=False)
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id or not self.created_on:
            self.created_on = datetime.datetime.today()
        return super(Player, self).save(*args, **kwargs) 

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