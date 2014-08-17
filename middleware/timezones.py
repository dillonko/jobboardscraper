import pytz

from django.utils import timezone


class TimezoneMiddleware(object):
    def process_request(self, request):
        # Manually setting timezone to Chicago
        # It's a best guess in the middle of America; it works OK for 
        # anonymous users without forcing them to enter their timezone 
        # as a session variable in the request
        tzname = 'America/Chicago'
        # tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
