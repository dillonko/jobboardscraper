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
