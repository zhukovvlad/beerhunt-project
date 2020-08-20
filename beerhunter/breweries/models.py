from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


class Brewery(TimeStampedModel):
    title = models.CharField('Title of brewery', max_length=255)
    slug = AutoSlugField(
        "Brewery Slug",
        unique=True,
        always_update=False,
        populate_from='title'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Brewery"
        verbose_name_plural = "Breweries"
