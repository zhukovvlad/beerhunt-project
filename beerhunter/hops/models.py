from django.db import models

from autoslug import AutoSlugField
from django_countries.fields import CountryField
from model_utils.models import TimeStampedModel


class AromaProfile(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        ordering = (
            'title',
        )


class Hop(TimeStampedModel):
    title = models.CharField("Title of Hop", max_length=255)
    slug = AutoSlugField(
        "Hop Slug",
        unique=True,
        always_update=False,
        populate_from='title'
    )
    country_of_origin = CountryField(
        "Country of Origin", blank=True
    )
    description = models.TextField("Description", blank=True)

    alpha_min = models.FloatField(null=True, blank=True)
    alpha_max = models.FloatField(null=True, blank=True)
    beta_min = models.FloatField(null=True, blank=True)
    beta_max = models.FloatField(null=True, blank=True)
    oil_min = models.FloatField(null=True, blank=True)
    oil_max = models.FloatField(null=True, blank=True)

    aroma_profile = models.ManyToManyField(
        to=AromaProfile,
        related_name='aroma_profile',
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = (
            'title',
        )
        verbose_name = "Hop"
        verbose_name_plural = "Hops"
