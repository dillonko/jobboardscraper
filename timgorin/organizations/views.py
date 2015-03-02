from django.views.generic import DetailView, ListView

from .models import Organization


class OrganizationDetailView(DetailView):
    model = Organization

organization_detail = OrganizationDetailView.as_view()


class OrganizationListView(ListView):
    model = Organization
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super(OrganizationListView, self).get_context_data(**kwargs)
        context['organization_count'] = Organization.objects.count()
        return context

organization_list = OrganizationListView.as_view()
