# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
from datetime import datetime

import pytz
from django.utils.text import slugify
from scrapy.exceptions import DropItem

from jobs.models import Board, Job
from organizations.models import Organization


class EslCafePipeline(object):

    def process_item(self, item, spider):
        item['board'] = self.get_or_create_board(item['board_title'], item['board_url'])
        item['title'] = item['title'][0]
        item['organization'] = self.get_or_create_organization(item['org_title'], item['org_email'])
        item['body'] = item['body'][0]
        item['pub_date'] = self.convert_to_datetime(item['pub_date'])

        """
        There is no native unique identifier for each job: a job with the same
        title might be a job we already scraped or it can be a new job with
        the same title (essentially a "reposted" job); therefore we pair the
        job title with the published date to determine if a job is "unique
        enough" to warrant a new entry
        """
        if not Job.objects.filter(title=item['title'], pub_date=item['pub_date']):
            item.save()
        else:
            raise DropItem('Job already exists.')

        """
        For every job that we save, we delete the oldest job because Heroku's
        free hobby-dev plan is limited to 10,000 rows.
        https://www.heroku.com/pricing
        """
        # job = Job.objects.all().last()
        # job.delete()

        return item

    def get_or_create_board(self, title, url):
        slug = slugify(title)
        try:
            return Board.objects.get(slug=slug)
        except Board.DoesNotExist:
            return Board.objects.create(title=title, slug=slug, url=url)

    def get_or_create_organization(self, title, email):
        title = title[0]
        slug = slugify(title)
        try:
            email = email[0].lower()
        except IndexError:
            email = ''
        try:
            return Organization.objects.get(slug=slug)
        except Organization.DoesNotExist:
            return Organization.objects.create(title=title, slug=slug, email=email)

    def convert_to_datetime(self, pub_list):
        """
        Converts messy datetime to timezone-aware datetime object;
        the webmaster seems to live in Northridge, CA, which is near Los
        Angeles and is in the Pacific Time timezone
        http://www.eslcafe.com/contact.html
        http://en.wikipedia.org/wiki/America/Los_Angeles
        """
        pub_string = pub_list[0]
        pub_string = re.sub('Date: ', '', pub_string)
        pub_string = re.sub('a.m.', 'AM', pub_string)
        pub_string = re.sub('p.m.', 'PM', pub_string)
        pub_string = re.sub(r'\n', '', pub_string)
        pub_date = datetime.strptime(pub_string, '%A, %d %B %Y, at %I:%M %p')
        pub_date = pytz.timezone('America/Los_Angeles').localize(pub_date)
        return pub_date
