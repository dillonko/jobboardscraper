from django.conf import settings
from django.views.generic import DetailView, ListView

from pure_pagination.mixins import PaginationMixin

from .models import Job


class JobDetailView(DetailView):
    model = Job


class JobListView(PaginationMixin, ListView):
    model = Job
    paginate_by = getattr(settings, 'PAGINATE_BY', 10)
