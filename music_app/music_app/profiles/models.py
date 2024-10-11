from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


# Create your models here.
class Profile(models.Model):
    MAX_LENGTH_USERNAME = 15
    MIN_LENGTH_USERNAME = 2
    username = models.CharField(
        max_length=MAX_LENGTH_USERNAME,
        validators=[
            MinLengthValidator(MIN_LENGTH_USERNAME),
            RegexValidator(
                regex=r"^[\w]+$",
                message="Ensure this value contains only letters, numbers, and underscore.",

            )], )
    email = models.EmailField()
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

