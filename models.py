from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import Permission, User
from .validators import validate_file_extension_image
from django.core.urlresolvers import reverse
from django.db import models
import datetime


class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    rating = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ]
    )

    album_cover = models.FileField(
        default='',
        validators=[validate_file_extension_image]
    )

    year_of_release = models.IntegerField(
        default=1900,
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.datetime.now().year)
        ]
    )

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + " - " + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, default=1)
    song_title = models.CharField(max_length=250, default="")

    def get_absolute_url(self):
        return reverse('music:song-add', kwargs={'pk': self.pk})

    def __str__(self):
        return self.song_title


