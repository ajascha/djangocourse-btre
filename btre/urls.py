from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # We are linking to the urls.py of pages app
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]
