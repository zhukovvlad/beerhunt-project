import pytest

from ..models import Beer

pytestmark = pytest.mark.django_db


def test__sts__():
    beer = Beer.objects.create(
        title="Stracchino",
        description="Semi-sweet cheese that goes well with starches.",
    )
    assert beer.__str__() == "Stracchino"
    assert str(beer) == "Stracchino"
