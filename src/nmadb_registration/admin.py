from django.contrib import admin
from django.utils.translation import ugettext as _

from nmadb_registration import models
from nmadb_utils import admin as utils
from nmadb_utils import actions


class TitleOnlyAdmin(utils.ModelAdmin):
    """ Administration for models, which have only title and id fields.
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


class MunicipalityAdmin(utils.ModelAdmin):
    """ Administration for municipality.
    """

    list_display = (
            'id',
            'title',
            'code',
            'town',
            'municipality_type',
            )

    list_filter = (
            'municipality_type',
            )

    search_fields = (
            'town',
            'code',
            )


class ConditionAdmin(utils.ModelAdmin):
    """ Administration for conditions.
    """

    list_display = (
            'id',
            'name',
            'result',
            )

    list_filter = (
            'result',
            )

    search_fields = (
            'name',
            'description',
            )


actions.register(_(u'Import schools'),
    'nmadb-registration-import-schools')
actions.register(_(u'Import sections'),
    'nmadb-registration-import-sections')
actions.register(_(u'Import municipalities'),
    'nmadb-registration-import-municipalities')

admin.site.register(models.School, TitleOnlyAdmin)
admin.site.register(models.Section, TitleOnlyAdmin)
admin.site.register(models.Municipality, MunicipalityAdmin)
admin.site.register(models.Address)
admin.site.register(models.Condition, ConditionAdmin)
