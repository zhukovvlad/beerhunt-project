import os
from django.db import models
from django.urls import reverse
from django.utils.timezone import now as timezone_now

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from autoslug import AutoSlugField
from django.conf import settings
from model_utils.models import TimeStampedModel
from uuid import uuid4

from beerhunter.breweries.models import Brewery


def beer_directory_path_with_uuid(instance, filename):
    now = timezone_now()
    extension = os.path.splitext(filename)[1]
    extension = extension.lower()
    uuid_for_url = uuid4()
    return f"{now:%Y/%m}/{uuid_for_url}{instance.pk}{extension}"


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

    image = models.ImageField(upload_to=beer_directory_path_with_uuid)

    image_icon = ImageSpecField(
        source='image',
        processors=[ResizeToFill(100, 100)],
        format='PNG',
        options={'quality': 60}
    )

    image_detail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(150, 150)],
        format='PNG',
        options={'quality': 70}
    )

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
