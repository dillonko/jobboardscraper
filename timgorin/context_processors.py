from django.contrib.sites.shortcuts import get_current_site


def site(request):
    """
    Gets current website and adds it to the request context.
    """
    return {'site': get_current_site(request)}
