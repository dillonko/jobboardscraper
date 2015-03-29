from search.forms import MySearchForm


def search_form(request):
    """
    Gets unbound search form class
    """
    return {'search_form': MySearchForm()}
