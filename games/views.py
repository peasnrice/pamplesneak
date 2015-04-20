from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from games.serializers import GameSerializer, PlayerSerializer, PhraseSerializer, UserSerializer, GroupSerializer
from rest_framework.decorators import detail_route, list_route
from games.models import Phrase, Game, Player, GamePlayerDetail
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

            user = request.user
            player = user.player

            player.hosted_count += 1
            player.game_count += 1
            if request.data['nickname'] != "":
                player.nickname = request.data['nickname']
            elif  player.nickname == "":
                player.nickname = player.user.username

            player.save()

            new_game = Game()
            new_game.host = player
            new_game.name = request.data['name']
            new_game.motto = request.data['motto']
            new_game.passcode = request.data['passcode']
            new_game.save()
            new_game.players.add(player)

            new_game_player_detail = GamePlayerDetail()
            new_game_player_detail.game = new_game
            new_game_player_detail.player = player
            new_game_player_detail.save()

            return Response({'status': 'game set', 'game_id': new_game.id})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @detail_route(methods=['post'])
    def join_game(self, request, pk=None):
        game = self.get_object()
        user = request.user
        player = user.player

        games = game.gpdgame.all()
        players = player.gpdplayer.all()

        if games and players:
            print "player already created"
            return Response({'status': 'player already joined'}, status=200) 

        else:
            print "new player game relationship created"
            new_game_player_detail = GamePlayerDetail()
            new_game_player_detail.game = game
            new_game_player_detail.player = player
            new_game_player_detail.save()
            return Response({'status': 'player added'}, status=200) 

class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows players to be viewed or edited.
    """ 
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


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