"""
A wrapper object that allows get_or_create of flatblock values for use as
template variables.

e.g.

{% if flatblocks.the-slug-name %}
    ...
{% endif %}

Will get or create a flatblock with the slug name given.

TODO: cacheing?
"""

from .models import FlatBlock
from django.core.cache import cache
from flatblocks import settings


class FlatBlockObject():
    def __getitem__(self, key):
        cache_key = settings.CACHE_PREFIX + key
        flatblock = cache.get(cache_key)

        if flatblock is None:
            fb, created = FlatBlock.objects.get_or_create(slug=key)
            flatblock = fb.content
            if not created:
                cache.set(cache_key, flatblock, settings.CACHE_TIMEOUT)
        return flatblock


def flatblocks(request):

    fbo = FlatBlockObject()
    return {'flatblocks': fbo}