import datetime

from django.utils.translation import ugettext_lazy as _

from nmadb_registration import models


def check_condition(name, **kwargs):
    """ Checks if condition specified in database is True.
    """

    condition = models.Condition.objects.get(name=name)
    if condition.result is None:
        variables = {
                'datetime': datetime,
                'date': datetime.date,
                'time': datetime.time,
                'today': datetime.date.today(),
                'now': datetime.datetime.now(),
                }
        variables.update(kwargs)
        return eval(condition.expression, variables)
    else:
        return condition.result
