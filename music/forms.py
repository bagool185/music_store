from django import forms
from django.contrib.auth.models import User

from .models import Album, Song


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_cover', 'year_of_release']


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_title']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
