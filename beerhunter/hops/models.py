from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


class Hop(TimeStampedModel):
    title = models.CharField("Title of Hop", max_length=255)
    slug = AutoSlugField(
        "Hop Slug",
        unique=True,
        always_update=False,
        populate_from='title'
    )
    description = models.TextField("Description", blank=True)

    def __str__(self):
        return self.title
