from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.core.urlresolvers import reverse_lazy

from .views import FaviconView, RobotsView, HomeView

urlpatterns = [

    # Admin password reset
    url(r'^admin/password_reset/$', auth_views.password_reset, name='admin_password_reset'),
    url(r'^admin/password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

    # Admin
    url(r'^admin/logout/$', auth_views.logout, {'next_page': reverse_lazy('admin:index')}),
    url(r'^admin/', admin.site.urls),

    # Public
    url(r'^jobs/', include('jobs.urls')),
    url(r'^organizations/', include('organizations.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^favicon\.ico$', FaviconView.as_view(), name='favicon'),
    url(r'^robots\.txt$', RobotsView.as_view(), name='robots'),
    url(r'^$', HomeView.as_view(), name='home'),

]


# Static/media for local development
if getattr(settings, 'DEBUG', False):
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
