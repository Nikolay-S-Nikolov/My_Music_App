from django.shortcuts import render, redirect

from music_app.album.models import Album
from music_app.profiles.models import Profile
from music_app.web.forms import CreateProfileForm


# Create your views here.
def get_profile():
    return Profile.objects.first()


def create_profile(request):
    form = CreateProfileForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('index')
    context = {
        "form": form,
        "no_nav": True,
    }
    return render(request, 'web/home-no-profile.html', context)


def index(request):
    if get_profile() is None:
        return create_profile(request)
    context = {
        "albums": Album.objects.all()
    }

    return render(request, "web/home-with-profile.html", context)
