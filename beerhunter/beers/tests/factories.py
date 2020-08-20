from django.template.defaultfilters import slugify

import factory
import factory.fuzzy

from ..models import Beer
from beerhunter.breweries.models import Brewery
# from beerhunter.breweries.tests.factories import BreweryFactory


class BeerFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    description = factory.Faker(
        'paragraph', nb_sentences=3, variable_nb_sentences=True
    )
    # brewery = factory.SubFactory(BreweryFactory)
    brewery = factory.Iterator(Brewery.objects.all())
    og = factory.fuzzy.FuzzyFloat(10.0, 25.0)
    ibu = factory.fuzzy.FuzzyFloat(0.0, 100.0)
    abv = factory.fuzzy.FuzzyFloat(3.5, 18.0)

    class Meta:
        model = Beer
