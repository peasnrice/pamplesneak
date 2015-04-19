from django.db import models

class Word(models.Model):
  creator = models.ForeignKey(Player)
  receiver = models.ForeignKey(Player)
  word_text = models.TextField()
  occurances = models.IntegerField(default=1)

