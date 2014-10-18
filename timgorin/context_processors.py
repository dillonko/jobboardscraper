from django.contrib.sites.shortcuts import get_current_site

from search.forms import MySearchForm


def site(request):
    """
    Gets current website
    """
    return {'site': get_current_site(request)}


def search_form(request):
    """
    Gets unbound search form class
    """
    return {'search_form': MySearchForm}
