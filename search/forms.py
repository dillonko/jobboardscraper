from django import forms

from haystack.forms import SearchForm


class MySearchForm(SearchForm):
    q = forms.CharField(required=False, label='Search', widget=forms.TextInput(attrs={'type': 'search', 'placeholder': 'Search jobs'}))

    def search(self):
        sqs = super(MySearchForm, self).search()
        return sqs
