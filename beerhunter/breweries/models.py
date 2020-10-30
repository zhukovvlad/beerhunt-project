import os
from uuid import uuid4
from django.db import models
from django.urls import reverse
from django.utils.timezone import now as timezone_now

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel
from django_countries.fields import CountryField
from django.utils.translation import gettext as _

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


def brewery_directory_path_with_uuid(instance, filename):
    now = timezone_now()
    extension = os.path.splitext(filename)[1]
    extension = extension.lower()
    uuid_for_url = uuid4()
    return f"{now:%Y/%m}/breweries/{uuid_for_url}{instance.pk}{extension}"


class Brewery(TimeStampedModel):
    title = models.CharField(_('Title of brewery'), max_length=255)
    slug = AutoSlugField(
        "Brewery Slug",
        unique=True,
        always_update=False,
        populate_from='title'
    )
    country_of_origin = CountryField(
        "Country of Origin", blank=True
    )

    image = models.ImageField(
        upload_to=brewery_directory_path_with_uuid,
        default='images/default/fermentation.png',
        null=True,
        blank=True
    )

    icon = ImageSpecField(
        source='image',
        processors=[ResizeToFill(100, 100)],
        format='PNG',
        options={'quality': 60}
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("breweries:BreweryDetail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Brewery"
        verbose_name_plural = "Breweries"
