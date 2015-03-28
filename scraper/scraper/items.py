# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# Although not documented anywhere, I *think* Scrapy falls under the
# use case of `AppRegistryNotReady` error "if you forget to call
# django.setup() in a standalone Python script."
# https://docs.djangoproject.com/en/1.7/ref/applications/#troubleshooting

import django
django.setup()

import scrapy
from scrapy.contrib.djangoitem import DjangoItem

from jobs.models import Job


class JobItem(DjangoItem):
    django_model = Job
    board_title = scrapy.Field()
    board_url = scrapy.Field()
    org_title = scrapy.Field()
    org_email = scrapy.Field()
