from django.db import models
from django.urls import reverse

from autoslug import AutoSlugField
from django.conf import settings
from model_utils.models import TimeStampedModel

from beerhunter.breweries.models import Brewery


class Beer(TimeStampedModel):
    title = models.CharField("Title of Beer", max_length=255)
    slug = AutoSlugField(
        "Beer Slug",
        unique=True,
        always_update=False,
        populate_from="title",
        allow_unicode=True,
    )
    description = models.TextField("Description", blank=True)
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE, related_name="brewered_by", null=True, blank=True)

    og = models.FloatField(null=True, blank=True)
    abv = models.FloatField(null=True, blank=True)
    ibu = models.FloatField(null=True, blank=True)

    hunter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("beers:BeerDetail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = "Beer"
        verbose_name_plural = "Beers"
