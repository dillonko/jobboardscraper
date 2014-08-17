from django.utils import timezone
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from scraper.items import JobItem


class EslCafeSpider(CrawlSpider):
    name = 'eslcafe'
    allowed_domains = ['eslcafe.com']
    start_urls = [
        'http://www.eslcafe.com/jobs/korea/'
    ]
    rules = [
        Rule(LinkExtractor(allow=['http://www\.eslcafe\.com/jobs/korea/index\.cgi\?read=\d+']), callback='parse_item')
    ]

    def parse_item(self, response):
        job = JobItem()
        job['title'] = response.xpath('/html/head/title/text()').extract()
        job['url'] = response.url
        job['pub_date'] = response.xpath('/html/body/p[3]/strong/br/following-sibling::text()[1]').extract()
        job['scrape_date'] = timezone.now()
        job['org_title'] = response.xpath('(/html/body/p)[3]/strong/big/text()').extract()
        job['org_email'] = response.xpath('(/html/body/p)[3]/strong/a/text()').extract()
        yield job
