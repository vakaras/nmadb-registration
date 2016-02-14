from django.contrib import admin
from django.utils.translation import ugettext as _

from nmadb_registration import models


class TitleOnlyAdmin(admin.ModelAdmin):
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


class MunicipalityAdmin(admin.ModelAdmin):
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


class ConditionAdmin(admin.ModelAdmin):
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


admin.site.register(models.School, TitleOnlyAdmin)
admin.site.register(models.Section, TitleOnlyAdmin)
admin.site.register(models.Municipality, MunicipalityAdmin)
admin.site.register(models.Address)
admin.site.register(models.Condition, ConditionAdmin)
