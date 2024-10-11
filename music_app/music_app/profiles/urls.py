from django.urls import path

from music_app.profiles.views import ProfileDetailsView, ProfileDeleteView

urlpatterns = (
    path('details/', ProfileDetailsView.as_view(), name='profile-details'),
    path('delete/', ProfileDeleteView.as_view(), name='profile-delete'),
)
