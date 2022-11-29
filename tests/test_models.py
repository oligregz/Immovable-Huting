import pytest
from immovablehutting.models import Immoble

@pytest.fixture
def immoble():
  return Immoble(title="Casa em Salinas")


@pytest.mark.django_db
def test_immoble_model(immoble):
  immoble.save()
  
  immobles_from_db = Immoble.objects.all()
  
  assert len(immobles_from_db) == 1
  assert immobles_from_db[0].title == "Casa em Salinas"