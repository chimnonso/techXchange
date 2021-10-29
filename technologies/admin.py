from django.contrib import admin
from .models import Technology, Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "company", "phone", "technology" )
    # list_display_links = ()
    # list_filter = ()

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("name",)
    # list_display_links = ()
    # list_filter = ()

admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Contact, ContactAdmin)
