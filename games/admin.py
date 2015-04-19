from django.contrib import admin
from games.models import Game, Player, Phrase, GamePlayerDetail
from games.forms import PlayerForm
 
class PlayerAdmin(admin.ModelAdmin):
  form = PlayerForm
  fieldsets = (
    (None, {'fields': ('nickname', 'hosted_count',
    'game_count', 'phrase_count', 'word_count', 
    'game_record', 'phrase_record', 'word_record','games')
    }),
  )

admin.site.register(Player, PlayerAdmin)
admin.site.register(Game)
admin.site.register(Phrase)
admin.site.register(GamePlayerDetail)