from django.conf.urls import patterns, include, url


urlpatterns = patterns('jobs.views',

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
