from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from nmadb_registration import models


def check_condition(name, **kwargs):
    """ Checks if condition specified in database is True.
    """

    condition = models.Condition.objects.get(name=name)
    if condition.result is None:
        now = timezone.now()
        variables = {
                'timezone': timezone,
                'today': now.date(),
                'now': now,
                }
        variables.update(kwargs)
        return eval(condition.expression, variables)
    else:
        return condition.result
