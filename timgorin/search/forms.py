from django import forms

from haystack.forms import SearchForm


class MySearchForm(SearchForm):
    q = forms.CharField(required=False, label='Search', widget=forms.TextInput(attrs={
        'type': 'search',
        'autocapitalize': 'words',
        'autocorrect': 'off',
        'placeholder': 'Search jobs',
        'class': 'form-control input-lg',
    }))

    def search(self):
        sqs = super(MySearchForm, self).search()

        if not self.is_valid():
            return self.no_query_found()

        sqs = sqs.order_by('-pub_date')

        return sqs
