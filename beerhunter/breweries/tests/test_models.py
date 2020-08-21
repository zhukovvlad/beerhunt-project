import pytest

# from ..models import Brewery
from .factories import BreweryFactory

pytestmark = pytest.mark.django_db


def test__str__():
    brewery = BreweryFactory()
    assert brewery.__str__() == brewery.title
    assert str(brewery) == brewery.title
