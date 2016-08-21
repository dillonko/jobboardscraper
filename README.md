# Job Board Scraper

**Job Board Scraper** collects, cleans, organizes, and indexes English teaching positions from an [existing online job board](http://www.eslcafe.com/jobs/korea/) once a day.

The code scrapes the job board with [Scrapy](http://scrapy.org/) and integrates it into a [Django](https://www.djangoproject.com/) website with an [Elasticsearch](https://www.elastic.co/) search index and a [PostgreSQL](https://www.postgresql.org/) database. The website is hosted on [Heroku](https://www.heroku.com/).

- [Code repository](https://github.com/richardcornish/jobboardscraper)
- [Deployed app](https://jobboardscraper.herokuapp.com/)

## Install

Prerequisites: [Python 3](https://www.python.org/), [SQLite](https://www.sqlite.org/), [pip](https://pip.pypa.io/), [virtualenv](https://virtualenv.readthedocs.io/), [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/), [Git](https://git-scm.com/).

```
$ mkvirtualenv jobboardscraper -p python3
$ git clone git@github.com:richardcornish/jobboardscraper.git
$ cd jobboardscraper/
$ pip install -r requirements.txt
$ cd jobboardscraper/
$ python manage.py migrate
$ python manage.py loaddata jobboardscraper/fixtures/*
$ python manage.py createsuperuser
$ python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000). Kill with `Ctrl+C`.

Setting a virtualenv default directory is usually a good idea:

```
$ setvirtualenvproject $WORKON_HOME/jobboardscraper/ ~/Sites/jobboardscraper/jobboardscraper/
$ cdproject
```

## Scrape

To run the spider to scrape the website:

```
$ cd scraper/
$ scrapy crawl eslcafe
```

## Search

Elasticsearch is required to build and update the search index. Assuming [Homebrew](http://brew.sh/) is installed, initial indexing:

```
$ brew install caskroom/cask/brew-cask
$ brew install Caskroom/cask/java
$ brew install elasticsearch
$ elasticsearch --config=/usr/local/opt/elasticsearch/config/elasticsearch.yml
$ python manage.py rebuild_index`
```

Future indexing:

```
$ python manage.py update_index
```

## Deploy

If you're using Heroku, deploying requires the Heroku Toolbelt:

- [Heroku Toolbelt](https://toolbelt.heroku.com/)

Heroku add-ons I installed:

- [Heroku Postgres](https://elements.heroku.com/addons/heroku-postgresql)
- [Heroku Scheduler](https://elements.heroku.com/addons/scheduler)
- [SearchBox Elasticsearch](https://elements.heroku.com/addons/searchbox)

Initial deploy:

```
$ heroku login
$ heroku create
$ heroku config:set SECRET_KEY='...' # replace with your own
$ heroku config:set DEBUG=''
$ heroku config:set WEB_CONCURRENCY='2'
$ heroku addons:create heroku-postgresql:hobby-dev
$ heroku addons:create scheduler:standard
$ heroku addons:create searchbox:starter
$ git push heroku master
$ heroku run python jobboardscraper/manage.py migrate
$ heroku run python jobboardscraper/manage.py loaddata jobboardscraper/jobboardscraper/fixtures/*
$ heroku run python jobboardscraper/manage.py createsuperuser
$ heroku open
```

Future deploys:

```
$ git push heroku master
```

After installation you can scrape the website and build the search index on Heroku:

```
$ heroku run '(cd jobboardscraper/scraper/ && scrapy crawl eslcafe)'
$ heroku run python jobboardscraper/manage.py rebuild_index
```

You can run the commands manually in the future, but more likely you will want to schedule a job with [Scheduler](https://scheduler.heroku.com/dashboard), which runs these commands every day to scrape and index:

- `(cd jobboardscraper/scraper/ && scrapy crawl eslcafe)`
- `python jobboardscraper/manage.py update_index`

You might need to edit the [SearchBox settings](https://dashboard.searchly.com/) on your Heroku dashboard to manually register your SearchBox API key and your search index's name if it doesn't work.

There is nothing specific to Heroku in the code; you can schedule a `cron` for the scraping and indexing commands if you prefer.