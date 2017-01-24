from django.contrib import admin
from .models import Album, Song


class SongInLine(admin.TabularInline):
    model = Song
    extra = 3


class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, { 'fields': ['album_title']}),
        ('Details', {'fields': ['artist', 'genre', 'year_of_release', 'album_cover'],
                     'classes': ['collapse']}),
    ]
    inlines = [SongInLine]
    list_display = ('album_title', 'artist', 'genre', 'year_of_release')
    list_filter = ['year_of_release', 'genre', 'artist']
    search_fields = ['album_title', 'artist']

admin.site.register(Album, AlbumAdmin)