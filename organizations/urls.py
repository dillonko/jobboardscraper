from django.conf.urls import patterns, include, url


urlpatterns = patterns('organizations.views',

    url(r'^(?P<slug>[-\w]+)/$',
        view='organization_detail',
        name='organization_detail'
    ),

    url(r'^$',
        view='organization_list',
        name='organization_list'
    ),

)
