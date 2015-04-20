from django.contrib.auth.models import User, Group
from rest_framework import serializers
from games.models import Phrase, Game, Player

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('url', 'id', 'user', 'nickname', 'created_on')

class GameSerializer(serializers.HyperlinkedModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)
    class Meta:
        model = Game
        fields = ('url', 'id', 'name', 'motto', 'created_on', 'players', 'host')

class PhraseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Phrase
        fields = ('url', 'phrase_text', 'created_on')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')