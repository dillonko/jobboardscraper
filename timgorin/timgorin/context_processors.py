from search.forms import MySearchForm


def search_form(request):
    return {
        'search_form': MySearchForm()
    }
