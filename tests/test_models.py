import pytest
from immovablehutting.models import Immoble

@pytest.fixture
def immoble():
  return Immoble(title="Casa em Salinas")


@pytest.mark.django_db
def test_immoble_model():
  immoble.save()