from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


class Beer(TimeStampedModel):
    title = models.CharField("Title of Beer", max_length=255)
    slug = AutoSlugField(
        "Beer Slug",
        unique=True,
        always_update=False,
        populate_from="title",
    )
    description = models.TextField("Description", blank=True)

    og = models.FloatField(null=True, blank=True)
    abv = models.FloatField(null=True, blank=True)
    ibu = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title
