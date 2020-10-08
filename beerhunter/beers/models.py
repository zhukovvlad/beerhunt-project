import os
from django.db import models
from django.urls import reverse
from django.utils.timezone import now as timezone_now

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from autoslug import AutoSlugField
import django.contrib.auth
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from model_utils.models import TimeStampedModel
from uuid import uuid4

from beerhunter.breweries.models import Brewery


def beer_directory_path_with_uuid(instance, filename):
    now = timezone_now()
    extension = os.path.splitext(filename)[1]
    extension = extension.lower()
    uuid_for_url = uuid4()
    return f"{now:%Y/%m}/{uuid_for_url}{instance.pk}{extension}"


class BeerManager(models.Manager):

    def all_with_related_instances(self):
        qs = self.get_queryset()
        qs = qs.select_related(
            'brewery', 'style'
        )
        return qs


class Beer(TimeStampedModel):
    title = models.CharField("Title of Beer", max_length=255, db_index=True)
    slug = AutoSlugField(
        "Beer Slug",
        unique=True,
        always_update=False,
        populate_from="title",
        allow_unicode=True,
    )
    version = models.CharField(max_length=140, blank=True, db_index=True)
    description = models.TextField("Description", blank=True)
    style = models.ForeignKey(
        to='Style',
        on_delete=models.SET_NULL,
        related_name="beers_with_style",
        null=True
    )
    brewery = models.ForeignKey(
        Brewery,
        on_delete=models.SET_NULL,
        related_name="brewered",
        null=True
    )

    og = models.FloatField(null=True, blank=True)
    abv = models.FloatField(null=True, blank=True)
    ibu = models.FloatField(null=True, blank=True)

    image = models.ImageField(
        upload_to=beer_directory_path_with_uuid,
        default='images/default/default_beer.png',
        blank=True
    )

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

    objects = BeerManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("beers:BeerDetail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ('title', )
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'version', 'brewery'],
                name='beer_constraint')
        ]
        verbose_name = "Beer"
        verbose_name_plural = "Beers"


class Style(models.Model):
    short_title = models.CharField(max_length=40, null=True, blank=True)
    title = models.CharField(max_length=140)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('short_title', )

    def __str__(self):
        return self.short_title


class VoteManager(models.Manager):
    def get_vote_or_unsaved_blank_vote(self, beer, user):
        try:
            return Vote.objects.get(
                beer=beer,
                user=user)
        except ObjectDoesNotExist:
            return Vote(
                beer=beer,
                user=user)


class Vote(models.Model):
    UP = 1
    DOWN = -1
    VALUE_CHOICES = (
        (UP, "UpVote"),
        (DOWN, "DownVote")
    )
    value = models.SmallIntegerField(
        choices=VALUE_CHOICES,
    )

    user = models.ForeignKey(
        django.contrib.auth.get_user_model(),
        on_delete=models.CASCADE
        )

    beer = models.ForeignKey(Beer, on_delete=models.CASCADE)

    voted_on = models.DateTimeField(auto_now=True)

    objects = VoteManager()

    class Meta:
        unique_together = ('user', 'beer', )


class BeerComment(TimeStampedModel):
    beer = models.ForeignKey(Beer, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True)
    title = models.CharField(max_length=80)
    body = models.TextField()

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.beer)
