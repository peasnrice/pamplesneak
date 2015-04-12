from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from games import views as game_views

router = routers.DefaultRouter()
router.register(r'games', game_views.GameViewSet)
router.register(r'phrases', game_views.PhraseViewSet)
router.register(r'users', game_views.UserViewSet)
router.register(r'groups', game_views.GroupViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/', include('allauth.urls')),
	url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/facebook/$', game_views.FacebookLogin.as_view(), name='fb_login'),
]