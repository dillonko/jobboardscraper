from django.conf.urls import patterns, include, url

from .views import MySearchView
from .forms import MySearchForm


urlpatterns = patterns('search.views',

    url(r'^$',
        MySearchView(form_class=MySearchForm),
        name='search'
    ),

)
