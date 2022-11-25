from django.contrib import admin
from django.urls import path

from immovablehutting.views import home, search

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home),
    path('search/', search),
]
