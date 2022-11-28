from .models import Immoble, Annoucement, Reserve
from rest_framework import serializers

class ImmobleSerializer(serializers.HyperLinkedModelSerializer):
  class Meta:
    model = Immoble
    fields = '__all__'

class AnnoucementSerializer(serializers.HyperLinkedModelSerializer):
  class Meta:
    model = Annoucement
    fields = '__all__'

class ReserveSerializer(serializers.HyperLinkedModelSerializer):
  class Meta:
    model = Reserve
    fields = '__all__'
