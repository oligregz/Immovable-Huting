import pytest
from immovablehutting.models import Immoble, Annoucement, Reserve

# -----------------------------------------Immoble Model case tests-----------------------------------------------
@pytest.fixture
def immoble():
  return Immoble(title="Casa em Salinas")


@pytest.mark.django_db
def test_immoble_model(immoble):
  immoble.save()
  
  immobles_from_db = Immoble.objects.all()
  
  assert len(immobles_from_db) == 1
  assert immobles_from_db[0].title == "Casa em Salinas"

# -----------------------------------------Annoucement Model case tests-----------------------------------------------
@pytest.fixture
def annoucement():
  return Annoucement(publishing_plataform="airbnb")


@pytest.mark.django_db
def test_announcement_model(annoucement):
  annoucement.save()
  
  annoucements_from_db = Annoucement.objects.all()
  
  assert Annoucement.objects.count() == 1
  assert annoucements_from_db[0].publishing_plataform == "airbnb"

# -----------------------------------------Reserve Model case tests-----------------------------------------------
# @pytest.fixture
# def reserve():
#   return Reserve(reserve_code=2022010)


# @pytest.mark.django_db
# def test_immoble_model(annoucement):
#   annoucement.save()
  
#   annoucements_from_db = Annoucement.objects.all()
  
#   assert Annoucement.objects.count() == 1
#   assert annoucements_from_db[0].publishing_plataform == "airbnb"

