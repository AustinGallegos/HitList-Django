from django.db import models
from django.core.validators import MinLengthValidator


class HitSubmissions(models.Model):
    track_id = models.CharField(
        max_length=22,
        validators=[MinLengthValidator(22)],
        null=False
    )
    track_name = models.CharField(
        max_length=200,
        null=False
    )
    artist_name = models.CharField(
        max_length=200,
        null=False
    )
    image_link = models.CharField(
        max_length=200,
        null=False
    )

    def __str__(self):
        return self.track_name


class CurrentHit(models.Model):
    track_id = models.CharField(
        max_length=22,
        validators=[MinLengthValidator(22)],
        null=False
    )
    track_name = models.CharField(
        max_length=200,
        null=False
    )
    artist_name = models.CharField(
        max_length=200,
        null=False
    )
    image_link = models.CharField(
        max_length=200,
        null=False
    )

    def __str__(self):
        return self.track_name
