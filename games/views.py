from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from games.serializers import GameSerializer, PhraseSerializer, UserSerializer, GroupSerializer
from rest_framework.decorators import detail_route
from games.models import Phrase, Game, Player
from datetime import datetime
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLogin

class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows games to be viewed or edited.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    def create(self, request):
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            print type(serializer)
            new_game = Game()
            new_game.name = request.data['name']
            new_game.motto = request.data['motto']
            new_game.passcode = request.data['passcode']
            new_game.save()

            new_player = Player()
            new_player.game = new_game
            new_player.nickname = request.data['nickname']
            new_player.user= request.user
            new_player.save()

            return Response({'status': 'game set', 'game_id': new_game.id})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

class PhraseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows game phrases to be viewed or edited.
    """
    queryset = Phrase.objects.all()
    serializer_class = PhraseSerializer

    def create(self, request):
        serializer = PhraseSerializer(data=request.data)
        if serializer.is_valid():
            print type(serializer)
            phrase = Phrase()
            phrase.phrase_text = request.data['phrase_text']
            phrase.save()
            return Response({'status': 'phrase set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class FacebookLogin(SocialLogin):
    adapter_class = FacebookOAuth2Adapter