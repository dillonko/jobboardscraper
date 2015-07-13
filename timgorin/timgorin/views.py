from django.conf import settings
from django.views.generic import TemplateView, RedirectView


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

home = HomeTemplateView.as_view()


class RobotsTemplateView(TemplateView):
    template_name = 'robots.txt'
    content_type = 'text/plain'

robots = RobotsTemplateView.as_view()


class FaviconRedirectView(RedirectView):
    url = '%simg/favicon.ico' % settings.STATIC_URL
    permanent = True

favicon = FaviconRedirectView.as_view()
