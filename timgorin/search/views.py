from django.conf import settings

from haystack.generic_views import SearchView
from pure_pagination.mixins import PaginationMixin

from .forms import MySearchForm


class MySearchView(PaginationMixin, SearchView):
    form_class = MySearchForm
    paginate_by = getattr(settings, 'PAGINATE_BY', 10)

    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        context['search_form'] = self.get_form_class()
        return context
