from django.core.validators import MinValueValidator
from django.db import models

from music_app.profiles.models import Profile


class Genre(models.TextChoices):
    POP_MUSIC = "Pop Music"
    JAZZ_MUSIC = "Jazz Music"
    RNB_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HOP_MUSIC = "Hip Hop Music"
    OTHER = "Other"


# Create your models here.
class Album(models.Model):
    MAX_ALBUM_NAME_LENGTH = 30
    MAX_ARTIST_LENGTH = 30
    MAX_GENRE_LENGTH = 30

    album_name = models.CharField(
        max_length=MAX_ALBUM_NAME_LENGTH,
        unique=True,
    )

    artist = models.CharField(
        max_length=MAX_ARTIST_LENGTH,
    )

    genre = models.CharField(
        max_length=MAX_GENRE_LENGTH,
        choices=Genre.choices
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=True,
        blank=True,
    )

    price = models.FloatField(
        validators=[MinValueValidator(0.0)]
    )

    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )
