# Mostly copied from another app's urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    # we want the url to look like /listings/<ID>, e.g. /listings/23:
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search')
]