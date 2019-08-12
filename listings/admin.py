from django.contrib import admin

from .models import Listing

# This class lets you modify the admin area for the listings app

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title') # These can be clicked; default = first entry only
    list_filter = ('realtor',) # Single entries need to be followed by a comma, otherwise error
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'zipcode')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)