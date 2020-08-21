from django.template.defaultfilters import slugify

import factory
import factory.fuzzy

from ..models import Brewery


class BreweryFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    country_of_origin = factory.Faker('country_code')

    class Meta:
        model = Brewery
