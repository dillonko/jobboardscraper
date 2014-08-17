#!/usr/bin/env python
import os
import sys

from django.conf import settings


if __name__ == "__main__":

    if getattr(settings, 'DEBUG', False):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "timgorin.settings.production")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "timgorin.settings.local")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
