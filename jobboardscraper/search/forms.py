from django import forms

from haystack.forms import SearchForm


class MySearchForm(SearchForm):
    q = forms.CharField(required=False, label='Query', widget=forms.TextInput(attrs={
        'type': 'search',
        'autocorrect': 'off',
        'class': 'form-control',
        'placeholder': 'Search jobs',
    }))

    def search(self):
        sqs = super(MySearchForm, self).search()
        if not self.is_valid():
            return self.no_query_found()
        sqs = sqs.order_by('-pub_date')
        return sqs

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(MySearchForm, self).__init__(*args, **kwargs)
        if self.request:
            if 'q' in self.request.GET:
                copy = self.request.GET.copy()
                self.fields['q'].initial = copy['q'].strip()
