import datetime

from django import forms
from django.utils.translation import ugettext as _

from django_db_utils.forms import SpreadSheetField
from pysheets.sheet import Sheet
from nmadb_registration import models


class ImportValidateRow(object):
    """ Checker, which checks if all columns are provided.
    """

    def __init__(self, required_columns, integer_columns=(),
            unique_columns=(), non_empty_columns=()):
        self.required_columns = required_columns
        self.non_empty_columns = non_empty_columns
        self.integer_columns = integer_columns
        self.unique_values = dict(
                (column, set()) for column in unique_columns)

    def __call__(self, sheet, row):
        """ Checks if row is valid.
        """
        new_row = {}
        for column, caption in self.required_columns.items():
            try:
                new_row[column] = row[caption]
            except KeyError as e:
                raise forms.ValidationError(
                        _(u'Missing column: \u201c{0}\u201d.').format(
                            e.message))

        try:
            for column in self.non_empty_columns:
                if not (new_row.get(column) or u'').strip():
                    raise forms.ValidationError(
                            _(u'{0} cannot be empty.').format(
                                self.required_columns[column]))
            for column in self.integer_columns:
                try:
                    new_row[column] = int(new_row[column])
                except ValueError:
                    raise forms.ValidationError(
                            _(u'{0} must be a number.').format(
                                self.required_columns[column]))
            for column, container in self.unique_values.items():
                if new_row[column] in container:
                    raise forms.ValidationError(
                            _(u'{0} values must be unique.').format(
                                self.required_columns[column]))
                else:
                    container.add(new_row[column])
        except forms.ValidationError as e:
            raise forms.ValidationError(
                    _(u'{0} Error occurred in {1} line. '
                    u'Sheet name is {2}.').format(
                        e.messages[0], len(sheet) + 2, sheet.name))
        return new_row


IMPORT_TITLE_ONLY_REQUIRED_COLUMNS = {
        u'id': _(u'ID'),
        u'title': _(u'Title'),
    }
def title_only_import_validate_sheet(spreadsheet, name, sheet):
    """ Creates sheet with correct columns.
    """
    sheet = Sheet(
            captions=(list(IMPORT_TITLE_ONLY_REQUIRED_COLUMNS.keys())))
    sheet.add_validator(
            ImportValidateRow(
                IMPORT_TITLE_ONLY_REQUIRED_COLUMNS,
                (u'id',),
                (u'id', u'title',),
                (u'id', u'title',),
                ),
            'insert')
    return sheet, name


class ImportTitleOnlyForm(forms.Form):
    """ Form for importing new title only models data.
    """

    spreadsheet = SpreadSheetField(
            sheet_name=_(u'Titles and IDs'),
            spreadsheet_constructor_args={
                'validators': {
                    'spreadsheet': [
                        (title_only_import_validate_sheet, 'add_sheet'),
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


IMPORT_MUNICIPALITIES_REQUIRED_COLUMNS = {
        u'id': _(u'ID'),
        u'town': _(u'Town'),
        u'municipality_type': _(u'Type'),
        u'code': _(u'Code'),
        }
def municipalities_import_validate_sheet(spreadsheet, name, sheet):
    """ Creates sheet with correct columns.
    """
    sheet = Sheet(
            captions=(list(IMPORT_MUNICIPALITIES_REQUIRED_COLUMNS.keys())))
    sheet.add_validator(
            ImportValidateRow(
                IMPORT_MUNICIPALITIES_REQUIRED_COLUMNS,
                (u'id', u'code',),
                (u'id', u'code',),
                (u'id', u'town', u'code',),
                ),
            'insert')
    return sheet, name


class ImportMunicipalitiesForm(forms.Form):
    """ Form for importing new title only models data.
    """

    spreadsheet = SpreadSheetField(
            sheet_name=_(u'Municipalities'),
            spreadsheet_constructor_args={
                'validators': {
                    'spreadsheet': [
                        (municipalities_import_validate_sheet, 'add_sheet'),
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
                        IMPORT_MUNICIPALITIES_REQUIRED_COLUMNS.values()))
            )


class AddressForm(forms.ModelForm):
    """ Form for address.
    """

    class Meta(object):
        model = models.Address
