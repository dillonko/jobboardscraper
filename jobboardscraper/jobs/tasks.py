from celery import shared_task
from haystack.management.commands import update_index
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


@shared_task
def scrape_task():
    """Celery task to scrape website with Scrapy.

    http://doc.scrapy.org/en/latest/topics/practices.html#run-scrapy-from-a-script
    """
    process = CrawlerProcess(get_project_settings())
    process.crawl('eslcafe', domain='eslcafe.com')
    process.start()


@shared_task
def index_task():
    """Celery task to index website with Haystack."""
    update_index.Command().handle(using=['default'])
