from django.utils import timezone
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

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

    board_title = u'Dave\'s ESL Cafe'
    board_url = u'http://www.eslcafe.com/jobs/korea/'

    def parse_item(self, response):
        job = JobItem()
        job['title'] = response.xpath('/html/head/title/text()').extract()
        job['body'] = response.xpath('/html/body/blockquote/font').extract()
        job['url'] = response.url
        job['pub_date'] = response.xpath('(/html/body/p)[3]/strong/br/following-sibling::text()').extract()
        job['scrape_date'] = timezone.now()
        job['board_title'] = self.board_title
        job['board_url'] = self.board_url
        job['org_title'] = response.xpath('(/html/body/p)[3]/strong/big/text()').extract()
        job['org_email'] = response.xpath('(/html/body/p)[3]/strong/a/text()').extract()
        yield job
