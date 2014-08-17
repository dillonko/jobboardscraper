from django.views.generic import DetailView, ListView

from organizations.models import Organization


class OrganizationDetailView(DetailView):
    model = Organization

organization_detail = OrganizationDetailView.as_view()


class OrganizationListView(ListView):
    model = Organization

organization_list = OrganizationListView.as_view()
