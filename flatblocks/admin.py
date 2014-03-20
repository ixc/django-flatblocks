from django.contrib import admin
from django.utils.html import strip_tags
from django.utils.text import Truncator
from django.template.defaultfilters import striptags

from flatblocks.models import FlatBlock


class FlatBlockAdmin(admin.ModelAdmin):
    """ Project-specific alterations -- no headers, no adding, fixed slugs. """
    ordering = ['slug', ]
    list_display = ('slug', 'content_summary')
    search_fields = ('slug', 'content')
    readonly_fields = ('slug',)
    fields = ('slug', 'content')
    actions = None

    def content_summary(self, block):
        return Truncator(strip_tags(block.content)).words(25)

    def has_add_permission(self, request):
        return False

admin.site.register(FlatBlock, FlatBlockAdmin)
