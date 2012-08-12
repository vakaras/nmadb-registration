from django.contrib import admin
from django.db import transaction
from django.core import urlresolvers
from django.utils.translation import ugettext as _
from django import shortcuts
from django.contrib import messages
from annoying.decorators import render_to

from nmadb_registration import forms, models


@admin.site.admin_view
@render_to('admin/file-form.html')
@transaction.commit_on_success
def import_schools(request):
    """ Imports schools.
    """
    if request.method == 'POST':
        form = forms.ImportTitleOnlyForm(request.POST, request.FILES)
        if form.is_valid():
            counter = 0
            for sheet in form.cleaned_data['spreadsheet']:
                for row in sheet:
                    school = models.School()
                    school.id = row[u'id']
                    school.title = row[u'title']
                    school.save()
                    counter += 1
            msg = _(u'{0} schools successfully imported.').format(counter)
            messages.success(request, msg)
            return shortcuts.redirect(
                    'admin:nmadb_registration_school_changelist')
    else:
        form = forms.ImportTitleOnlyForm()
    return {
            'admin_index_url': urlresolvers.reverse('admin:index'),
            'app_url': urlresolvers.reverse(
                'admin:app_list',
                kwargs={'app_label': 'nmadb_registration'}),
            'app_label': _(u'NMADB Registration'),
            'form': form,
            }


@admin.site.admin_view
@render_to('admin/file-form.html')
@transaction.commit_on_success
def import_sections(request):
    """ Imports sections.
    """
    if request.method == 'POST':
        form = forms.ImportTitleOnlyForm(request.POST, request.FILES)
        if form.is_valid():
            counter = 0
            for sheet in form.cleaned_data['spreadsheet']:
                for row in sheet:
                    section = models.Section()
                    section.id = row[u'id']
                    section.title = row[u'title']
                    section.save()
                    counter += 1
            msg = _(u'{0} sections successfully imported.').format(counter)
            messages.success(request, msg)
            return shortcuts.redirect(
                    'admin:nmadb_registration_section_changelist')
    else:
        form = forms.ImportTitleOnlyForm()
    return {
            'admin_index_url': urlresolvers.reverse('admin:index'),
            'app_url': urlresolvers.reverse(
                'admin:app_list',
                kwargs={'app_label': 'nmadb_registration'}),
            'app_label': _(u'NMADB Registration'),
            'form': form,
            }
