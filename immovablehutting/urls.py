from rest_framework import routers
from django.urls import path, include

from .views import ImmobleViewSet, AnnoucementViewSet, ReserveViewSet

router = routers.DefaultRouter()
# aqui lista todos valores dos campos passados através de um url
router.register(r'immobles', ImmobleViewSet)
router.register(r'annoucements', AnnoucementViewSet)
router.register(r'reserves', ReserveViewSet)

urlpatterns = [
  path("api/", include(router.urls)),
]
