from django.conf.urls import url
from . import views

app_name='music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'album-add/$', views.AlbumCreate.as_view(), name='album-add'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^song-add/(?P<pk>[0-9]+)/$', views.SongAdd.as_view(), name='song-add'),
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
    url(r'^http://www.youtube.com/results?search_query=(?P<youtube_query>[\w\[\]%])/$', views.youtube_redirect,
        name='youtube')
]
