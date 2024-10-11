from django.urls import path, include

from music_app.album.views import AlbumAddView, AlbumDetailView, AlbumEditView, AlbumDeleteView

urlpatterns = (
    path('add/', AlbumAddView.as_view(), name='add-album'),
    path('<int:pk>/', include([
        path('details/', AlbumDetailView.as_view(), name='details-album'),
        path('edit/', AlbumEditView.as_view(), name='edit-album'),
        path('delete/', AlbumDeleteView.as_view(), name='delete-album'),

    ])),
)
