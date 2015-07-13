from django.conf.urls import url

from .views import MySearchView


urlpatterns = [

    url(r'^$', MySearchView.as_view(), name='search'),

]
