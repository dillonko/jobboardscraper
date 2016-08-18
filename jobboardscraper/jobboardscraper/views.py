from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import TemplateView, RedirectView


class HomeView(TemplateView):
    template_name = 'home.html'


class FaviconView(RedirectView):
    url = staticfiles_storage.url('img/favicon.ico')
    permanent = True


class RobotsView(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'
