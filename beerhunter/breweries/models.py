from django.db import models
from django.urls import reverse

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel
from django_countries.fields import CountryField
from django.utils.translation import gettext as _


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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("breweries:BreweryDetail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Brewery"
        verbose_name_plural = "Breweries"
