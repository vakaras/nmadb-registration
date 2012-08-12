import datetime

from django import forms
from django.utils.translation import ugettext as _

from django_db_utils.forms import SpreadSheetField
from pysheets.sheet import Sheet


IMPORT_TITLE_ONLY_REQUIRED_COLUMNS = {
        u'id': _(u'ID'),
        u'title': _(u'Title'),
    }


def school_import_validate_row(sheet, row):
    """ Checks if row is valid.
    """
    new_row = {}
    for column, caption in IMPORT_TITLE_ONLY_REQUIRED_COLUMNS.items():
        try:
            new_row[column] = row[caption]
        except KeyError as e:
            raise forms.ValidationError(
                    _(u'Missing column: \u201c{0}\u201d.').format(
                        e.message))

    try:
        if not (new_row.get(u'id') or u'').strip():
            raise forms.ValidationError(
                    _(u'ID cannot be empty.'))
        if not (new_row.get(u'id') or u'').strip():
            raise forms.ValidationError(
                    _(u'Title cannot be empty.'))
    except forms.ValidationError as e:
        raise forms.ValidationError(
                _(u'{0} Error occurred in {1} line. '
                u'Sheet name is {2}.').format(
                    e.messages[0], len(sheet) + 2, sheet.name))
    return new_row


def school_import_validate_sheet(spreadsheet, name, sheet):
    """ Creates sheet with correct columns.
    """
    sheet = Sheet(
            captions=(list(IMPORT_TITLE_ONLY_REQUIRED_COLUMNS.keys())))
    sheet.add_validator(school_import_validate_row, 'insert')
    return sheet, name


class ImportTitleOnlyForm(forms.Form):
    """ Form for importing new title only models data.
    """

    spreadsheet = SpreadSheetField(
            sheet_name=_(u'Titles and IDs'),
            spreadsheet_constructor_args={
                'validators': {
                    'spreadsheet': [
                        (school_import_validate_sheet, 'add_sheet'),
                        ],
                    },
                },
            label=_(u'Spreadsheet document'),
            required=True,
            help_text=_(
                u'Please select spreadsheet file. '
                u'Required columns are: {0}.').format(
                    u','.join(
                        _(u'\u201c{0}\u201d').format(caption)
                        for caption in
                        IMPORT_TITLE_ONLY_REQUIRED_COLUMNS.values()))
            )
