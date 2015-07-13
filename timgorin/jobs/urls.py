from django.conf.urls import url

from .views import JobDetailView, JobListView


urlpatterns = [

    url(r'^(?P<pk>[\d]+)/$', JobDetailView.as_view(), name='job_detail'),

    url(r'^$', JobListView.as_view(), name='job_list'),

]
