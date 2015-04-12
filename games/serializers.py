from django.contrib.auth.models import User, Group
from rest_framework import serializers
from games.models import Phrase, Game

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('url', 'name', 'motto')

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