from django.conf.urls import patterns, include, url


urlpatterns = patterns('jobs.views',

    # Detail
    url(r'^(?P<pk>[\d]+)/$',
        view='job_detail',
        name='job_detail'
    ),

    # List, paginated
    url(r'^page/(?P<page>[0-9]+)/$',
        view='job_list',
        name='job_list_pages'
    ),

    # List
    url(r'^$',
        view='job_list',
        name='job_list'
    ),

)
