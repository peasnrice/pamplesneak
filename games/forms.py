from django import forms
from django.contrib import admin
                                                                
from games.models import Player, Game

from django.db.models.fields.related import ManyToManyRel
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
                                                                
class PlayerForm(forms.ModelForm):                             
                                                                
  games = forms.ModelMultipleChoiceField(Game.objects.all(),                                        
# Add this line to use the double list widget                  
#    widget=admin.widgets.FilteredSelectMultiple('Games', False),
    required=False,                                            
  ) 
     
  def __init__(self, *args, **kwargs):                         
    super(PlayerForm, self).__init__(*args, **kwargs)
    if self.instance.pk:
      #if this is not a new object, we load related games                                       
      self.initial['games'] = self.instance.games.values_list('pk', flat=True)
      rel = ManyToManyRel(Game)
      self.fields['games'].widget = RelatedFieldWidgetWrapper(self.fields['games'].widget, rel, admin.site)   

  def save(self, *args, **kwargs):                             
    instance = super(PlayerForm, self).save(*args, **kwargs)   
    if instance.pk:
      for game in instance.games.all():
        if game not in self.cleaned_data['games']:            
          # we remove games which have been unselected 
          instance.games.remove(game)
      for game in self.cleaned_data['games']:                  
        if game not in instance.games.all():                   
          # we add newly selected games
          instance.games.add(game)      
    return instance