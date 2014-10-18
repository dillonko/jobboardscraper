from django.contrib.sites.shortcuts import get_current_site

from search.forms import MySearchForm


def site(request):
    """
    Gets current website and adds it to the request context.
    """
    return {'site': get_current_site(request)}


def search_form(request):
    """
    Gets current website and adds it to the request context.
    """
    return {'search_form': MySearchForm}
