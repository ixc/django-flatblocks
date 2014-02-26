from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.cache import cache

from flatblocks.settings import CACHE_PREFIX


@python_2_unicode_compatible
class FlatBlock(models.Model):
    """
    Think of a flatblock as a flatpage but for just part of a site. It's
    basically a piece of content with a given name (slug).
    """
    slug = models.CharField(max_length=255, unique=True,
                verbose_name=_('Slug'),
                help_text=_("A unique name used for reference in the templates"))
    content = models.TextField(verbose_name=_('Content'), blank=True,
                null=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        super(FlatBlock, self).save(*args, **kwargs)
        # Now also invalidate the cache used in the templatetag
        cache.delete('%s%s' % (CACHE_PREFIX, self.slug, ))

    class Meta:
        verbose_name = _('Flat block')
        verbose_name_plural = _('Flat blocks')
