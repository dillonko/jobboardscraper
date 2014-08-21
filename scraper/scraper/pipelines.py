# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import pytz
from datetime import datetime

from django.utils.text import slugify
from scrapy.exceptions import DropItem

from jobs.models import Job
from organizations.models import Organization


class ScraperPipeline(object):

    def process_item(self, item, spider):
        item['title'] = item['title'][0]
        item['organization'] = self.get_organization(item['org_title'], item['org_email'])
        item['body'] = item['body'][0]
        item['pub_date'] = self.get_datetime(item['pub_date'])
        if not Job.objects.filter(title=item['title'], pub_date=item['pub_date']):
            item.save()
        else:
            raise DropItem('Job already exists.')
        return item

    def get_organization(self, title, email):
        title = title[0]
        slug = slugify(title)
        try:
            email = email[0].lower()
        except IndexError:
            email = ''
        if not Organization.objects.filter(slug=slug):
            return Organization.objects.create(title=title, slug=slug, email=email)
        else:
            return Organization.objects.get(slug=slug)

    def get_datetime(self, pub_list):
        pub_string = pub_list[0]
        pub_string = re.sub('Date: ', '', pub_string)
        pub_string = re.sub('a.m.', 'AM', pub_string)
        pub_string = re.sub('p.m.', 'PM', pub_string)
        pub_string = re.sub(r'\n', '', pub_string)
        pub_date = datetime.strptime(pub_string, '%A, %d %B %Y, at %I:%M %p')
        pub_date = pytz.timezone('America/Los_Angeles').localize(pub_date)
        return pub_date
