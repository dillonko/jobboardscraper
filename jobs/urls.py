from django.conf.urls import patterns, include, url


urlpatterns = patterns('jobs.views',

    # Detail
    url(r'^(?P<pk>[\d]+)/$',
        view='job_detail',
        name='job_detail'
    ),

    # List
    url(r'^$',
        view='job_list',
        name='job_list'
    ),

)
