from django.shortcuts import render
from .models import Immoble, Annoucement, Reserve
from .serializer import ImmobleSerializer, AnnoucementSerializer, ReserveSerializer
from rest_framework import viewsets

class ImmobleViewSet(viewsets.ModelViewSet):
  queryset = Immoble.objects.all()
  serializer_class = ImmobleSerializer

class AnnoucementViewSet(viewsets.ModelViewSet):
  queryset = Annoucement.objects.all()
  serializer_class = AnnoucementSerializer
  
  def destroy(self, request, *args, **kwargs):
    if(request.user == "admin"):
      annoucement = self.get_object()
      annoucement.delete()
      response_message={"message": "deleted"}
    else:
      response_message={"message": "Not Allowed"}
    return response_message
  
class ReserveViewSet(viewsets.ModelViewSet):
  queryset = Reserve.objects.all()
  serializer_class = ReserveSerializer
  http_method_names = ['get', 'post', 'head']