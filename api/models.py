from django.db import models
from django.core.validators import RegexValidator


class Photo(models.Model):
    title = models.CharField(max_length=255)
    album_id = models.PositiveIntegerField()
    width = models.PositiveSmallIntegerField(default=0)
    height = models.PositiveSmallIntegerField(default=0)
    color = models.CharField(
        max_length=7,
        validators=[RegexValidator(r"^#(?:[0-9a-fA-F]{3}){1,2}$")],
        help_text="Dominant color as hex code"
    )
    image = models.ImageField()
