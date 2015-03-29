from django.shortcuts import render_to_response

from haystack.views import SearchView


class MySearchView(SearchView):

    def create_response(self):
        """
        Copied from django-haystack to simply customize the `search_form` context variable
        https://github.com/toastdriven/django-haystack/blob/master/haystack/views.py#L126
        """
        (paginator, page_obj) = self.build_page()

        context = {
            'query': self.query,
            'search_form': self.form,
            'page_obj': page_obj,
            'paginator': paginator,
            'suggestion': None,
        }

        if self.results and hasattr(self.results, 'query') and self.results.query.backend.include_spelling:
            context['suggestion'] = self.form.get_suggestion()

        context.update(self.extra_context())
        return render_to_response(self.template, context, context_instance=self.context_class(self.request))
