from django import forms
from django.forms import modelform_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from music_app.album.models import Album
from music_app.profiles.models import Profile


# Create your views here.

class AlbumFieldsMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["album_name"].widget.attrs = {"placeholder": "Album Name"}
        form.fields["artist"].widget.attrs = {"placeholder": "Artist"}
        form.fields["description"].widget.attrs = {"placeholder": "Description"}
        form.fields["image_url"].widget.attrs = {"placeholder": "Image URL"}
        form.fields['price'].widget = forms.TextInput(attrs={'placeholder': 'Price'})
        return form


class AlbumAddView(AlbumFieldsMixin, views.CreateView):
    queryset = Album.objects.all()
    fields = ("album_name", "artist", "genre", "description", "image_url", "price")
    template_name = "album/album-add.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.instance.owner_id = Profile.objects.first().pk
        return super().form_valid(form)


class AlbumDetailView(AlbumFieldsMixin, views.DetailView):
    queryset = Album.objects.all()
    fields = ("album_name", "artist", "genre", "description", "image_url", "price")
    template_name = "album/album-details.html"


class AlbumEditView(AlbumFieldsMixin, views.UpdateView):
    queryset = Album.objects.all()
    fields = ("album_name", "artist", "genre", "description", "image_url", "price")
    template_name = "album/album-edit.html"
    success_url = reverse_lazy("index")


class AlbumDeleteView(views.DeleteView):
    queryset = Album.objects.all()
    form_class = modelform_factory(
        model=Album,
        fields=("album_name", "artist", "genre", "description", "image_url", "price"),
    )
    template_name = "album/album-delete.html"
    success_url = reverse_lazy("index")

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs["readonly"] = "readonly"
        return form

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs
