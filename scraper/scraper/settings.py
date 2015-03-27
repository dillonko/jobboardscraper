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
# USER_AGENT = 'scraper (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'scraper.pipelines.EslCafePipeline': 300,
}

# Although not documented anywhere, I *think* Scrapy falls under the
# use case of `AppRegistryNotReady` error "if you forget to call
# django.setup() in a standalone Python script."
# https://docs.djangoproject.com/en/1.7/ref/applications/#troubleshooting

import django
django.setup()

# Set Django settings module
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'timgorin.settings'
