from django.conf.urls.defaults import patterns, url


urlpatterns = patterns(
    'nmadb_registration.views',
    url(r'^school/import/$', 'import_schools',
        name='nmadb-registration-import-schools',),
    )
