from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from music_app.profiles.models import Profile


# Create your views here.
class ProfileObjectMixin:
    def get_object(self, queryset=None):
        return Profile.objects.first()


class ProfileDetailsView(ProfileObjectMixin,views.DetailView):
    template_name = "profile/profile-details.html"


class ProfileDeleteView(ProfileObjectMixin,views.DeleteView):
    template_name = "profile/profile-delete.html"
    success_url = reverse_lazy("index")
