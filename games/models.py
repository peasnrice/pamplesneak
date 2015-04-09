from django.db import models
import datetime

class Game(models.Model):
    name = models.CharField(max_length=50)
    motto = models.CharField(max_length=100)
    created_on = models.DateTimeField(editable=False)
    def __str__(self):
        return self.name

class Phrase(models.Model):
    phrase_text = models.CharField(max_length=200)
    created_on  = models.DateTimeField(editable=False)
    def __str__(self):
        return self.phrase_text
        
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id or not self.created_on:
            self.created_on = datetime.datetime.today()
        return super(Phrase, self).save(*args, **kwargs)   
