# Job board scraper

This code scrapes a job board daily with [Scrapy](http://scrapy.org/) and integrates it into a [Django](https://www.djangoproject.com/) website with a [PostgreSQL](http://www.postgresql.org/) database. The website is hosted on [Heroku](https://www.heroku.com/).

The deployed website: [http://timgorin.herokuapp.com](http://timgorin.herokuapp.com/)

## Scrapy notes

To run the spider to scrape the website:

1. `cd ~/Sites/timgorin/`
2. `workon timgorin`
3. `cd scraper`
4. `scrapy crawl eslcafe`

## Elasticsearch notes

To update the index to search the website:

1. Install [Java JDK and Java JRE](http://www.oracle.com/technetwork/java/javase/downloads/index.html)
2. `brew install elasticsearch`
3. `elasticsearch --config=/usr/local/opt/elasticsearch/config/elasticsearch.yml`
5. `cd ~/Sites/timgorin/`
4. `workon timgorin`
6. `python manage.py rebuild_index` (or `update_index` subsequently)

## Heroku notes

Heroku add-ons I used:

- [Heroku Scheduler](https://addons.heroku.com/scheduler)
- [Heroku Postgres](https://addons.heroku.com/heroku-postgresql)
- [Bonsai Elasticsearch](https://addons.heroku.com/bonsai)

The Scheduler needs to run a tasks to scrape the website and to update the search index.

- `(cd scraper && scrapy crawl eslcafe)`
- `python manage.py update_index`

Resources that helped me:

- [hk0weather](https://github.com/sammyfung/hk0weather) Hong Kong weather data project by [Sammy Fung](http://sammy.hk/)
- [Python, Web scraping and content management: Scrapy and Django](http://www.slideshare.net/sammyfung/python-web-scraping-and-content-management-scrapy-and-django)
- [Open Data, Open Government](http://www.slideshare.net/sammyfung/hk0weather-barcamp)
- New Coder "[Web scraper](http://newcoder.io/scrape/)" tutorial by [Lynn Root](http://www.roguelynn.com/)
- [Getting started with Django on Heroku](https://devcenter.heroku.com/articles/getting-started-with-django)
