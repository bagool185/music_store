from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.utils.http import urlencode
from django.views.generic import View
from django.views import generic
from .models import Album, Song
from django.db.models import Q
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        query = self.request.GET.get('q')

        if query:
            return Album.objects.filter(Q(album_title__istartswith=query) | Q(artist__istartswith=query))
        else:
            return Album.objects.filter()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_cover', 'year_of_release']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre',  'album_cover', 'year_of_release']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class SongAdd(CreateView):
    model = Song
    fields = ['album', 'song_title']


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

#   display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

#   process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})


def youtube_redirect(request, query):
    return HttpResponseRedirect('www.youtube.com/results?search_query=' + urlencode(query))