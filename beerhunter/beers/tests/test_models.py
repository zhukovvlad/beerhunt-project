import pytest

# from ..models import Beer
from .factories import BeerFactory

pytestmark = pytest.mark.django_db


def test__str__():
    beer = BeerFactory()
    assert beer.__str__() == beer.title
    assert str(beer) == beer.title
