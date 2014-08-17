# -*- coding: utf-8 -*-

# Scrapy settings for scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scraper'

SPIDER_MODULES = ['scraper.spiders']
NEWSPIDER_MODULE = 'scraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scraper (+http://www.yourdomain.com)'


# Set DJANGO_SETTINGS_MODULE
from django.conf import settings
if getattr(settings, 'DEBUG', False):
    import os, sys
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "timgorin.settings.local")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "timgorin.settings.production")
    path = os.path.join(os.path.dirname(__file__),'../timgorin')
    sys.path.append(os.path.abspath(path))

ITEM_PIPELINES = {
    'scraper.pipelines.ScraperPipeline': 300,
}
