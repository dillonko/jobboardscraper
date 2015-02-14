from django.views.generic import DetailView, ListView

from .models import Organization


class OrganizationDetailView(DetailView):
    model = Organization

organization_detail = OrganizationDetailView.as_view()


class OrganizationListView(ListView):
    model = Organization
    paginate_by = 50

organization_list = OrganizationListView.as_view()
