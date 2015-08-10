from django.conf import settings

from haystack.generic_views import SearchView
from pure_pagination.mixins import PaginationMixin

from .forms import MySearchForm


class MySearchView(PaginationMixin, SearchView):
    form_class = MySearchForm
    paginate_by = getattr(settings, 'PAGINATE_BY', 10)
