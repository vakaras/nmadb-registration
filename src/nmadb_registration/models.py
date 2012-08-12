from django.db import models
from django.utils.translation import ugettext_lazy as _


class School(models.Model):
    """ School information.
    """

    title = models.CharField(
            max_length=80,
            blank=False,
            verbose_name=_(u'Title'),
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


class Address(models.Model):
    """ Address in Lithuania.
    """

    postal_code = models.CharField(
            max_length=10,
            ) # TODO: Change to postal code.

    class Meta(object):
        verbose_name = _(u'address')
        verbose_name_plural = _(u'addresses')

    def __unicode__(self):
        return self.postal_code
