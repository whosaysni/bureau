from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _


@python_2_unicode_compatible
class EntityBase(models.Model):

    name = models.CharField(
        _('Name'), help_text=_('Physical name of entity.'),
        max_length=128)
    logical_name = models.CharField(
        _('Logical Name'),
        help_text=_('Logical name of entity.'), max_length=256,
        blank=True)
    comment = models.TextField(
        _('Comment'),
        help_text=_('Short comment of entity.'), blank=True)
    description = models.TextField(
        _('Description'),
        help_text=_('Detailed description of entity.'),
        blank=True)
    pos = models.IntegerField(
        _('Position'), default=1000)

    def __str__(self):
        ret = self.name
        if self.logical_name:
            ret += ' %s' %(self.logical_name)
        return ret

    class Meta:
        abstract = True
