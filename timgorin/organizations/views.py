from django.views.generic import DetailView, ListView

from pure_pagination.mixins import PaginationMixin

from .models import Organization


class OrganizationDetailView(DetailView):
    model = Organization


class OrganizationListView(PaginationMixin, ListView):
    model = Organization
    paginate_by = 50
