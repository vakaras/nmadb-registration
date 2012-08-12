from django.contrib import admin
from django.utils.translation import ugettext as _

from nmadb_registration import models
from nmadb_utils import admin as utils
from nmadb_utils import actions


class SchoolAdmin(utils.ModelAdmin):
    """ Administration for school.
    """

    list_display = (
            'id',
            'title',
            )

    search_fields = (
            'id',
            'title',
            )

    sheet_mapping = (
            (_(u'ID'), ('id',)),
            (_(u'Title'), ('title',)),
            )


actions.register(_(u'Import schools'), 'nmadb-registration-import-schools')

admin.site.register(models.School, SchoolAdmin)
admin.site.register(models.Address)
