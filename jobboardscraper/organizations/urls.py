from django.conf.urls import url

from .views import OrganizationDetailView, OrganizationListView


urlpatterns = [

    url(r'^(?P<slug>[-\w]+)/$', OrganizationDetailView.as_view(), name='organization_detail'),

    url(r'^$', OrganizationListView.as_view(), name='organization_list'),

]
