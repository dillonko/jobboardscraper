# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.djangoitem import DjangoItem

from jobs.models import Job


class JobItem(DjangoItem):
    django_model = Job
    org_title = scrapy.Field()
    org_email = scrapy.Field()
