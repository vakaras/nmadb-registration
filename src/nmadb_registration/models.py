from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_db_utils.models import PostalNumberField


class School(models.Model):
    """ School information.
    """

    title = models.CharField(
            max_length=80,
            blank=False,
            verbose_name=_(u'title'),
            unique=True,
            )

    class Meta(object):
        ordering = [u'title']
        verbose_name = _(u'school')
        verbose_name_plural = _(u'schools')

    def __unicode__(self):
        return self.title


class Section(models.Model):
    """ NMA section.
    """

    title = models.CharField(
            max_length=45,
            unique=True,
            verbose_name=_(u'title'),
            )

    class Meta(object):
        ordering = [u'title',]
        verbose_name = _(u'section')
        verbose_name_plural = _(u'sections')

    def __unicode__(self):
        return unicode(self.title)


class Municipality(models.Model):
    """ Information about municipality.
    """

    MUNICIPALITY_TYPES = (
            (u'T', _(u'town')),
            (u'D', _(u'district')),
            )

    town = models.CharField(
            max_length=45,
            verbose_name=_(u'town'),
            )

    municipality_type = models.CharField(
            max_length=2,
            choices=MUNICIPALITY_TYPES,
            blank=True,
            verbose_name=_(u'type'),
            )

    code = models.PositiveSmallIntegerField(
            verbose_name=_(u'code'),
            )

    def title(self):
        """ Return generated title of municipality.
        """

        if self.municipality_type:
            return u'{0} {1}'.format(
                    self.town, self.get_municipality_type_display())
        else:
            return self.town
    title.short_description = _(u'title')

    class Meta(object):
        ordering = [u'town', u'municipality_type',]
        verbose_name = _(u'municipality')
        verbose_name_plural = _(u'municipalities')

    def __unicode__(self):
        return self.title


class Address(models.Model):
    """ Address in Lithuania.
    """

    postal_code = PostalNumberField(
            verbose_name=_(u'postal code'),
            help_text=_(u'Can be looked up in www.post.lt.'),
            )

    municipality = models.ForeignKey(
            Municipality,
            verbose_name=_(u'municipality'),
            )

    living_area = models.CharField(
            max_length=128,
            verbose_name=_(u'living area'),
            help_text=_(u'For example, Vilnius or Smilgi\u0173 kaimas'),
            )

    street = models.CharField(
            max_length=128,
            verbose_name=_(u'street'),
            help_text=_(u'Street name. For example, A. Vivulskio.'),
            )

    house_number = models.PositiveSmallIntegerField(
            verbose_name=_(u'house number'),
            )

    house_letter = models.CharField(
            max_length=2,
            verbose_name=_(u'house letter'),
            blank=True,
            help_text=_(u'For example, B.'),
            )

    flat_number = models.PositiveSmallIntegerField(
            verbose_name=_(u'flat number'),
            blank=True,
            )

    class Meta(object):
        verbose_name = _(u'address')
        verbose_name_plural = _(u'addresses')

    def __unicode__(self):
        return self.postal_code
