from haystack.generic_views import SearchView

from .forms import MySearchForm


class MySearchView(SearchView):
    form_class = MySearchForm

    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        context['search_form'] = self.get_form_class()
        return context
