# Job board scraper

This code scrapes a [job board](http://www.eslcafe.com/jobs/korea/) with [Scrapy](http://scrapy.org/) every day and integrates it into a [Django](https://www.djangoproject.com/) website with an [Elasticsearch](http://www.elasticsearch.org/) search index and a [PostgreSQL](http://www.postgresql.org/) database. The website is hosted on [Heroku](https://www.heroku.com/).

[https://timgorin.herokuapp.com](https://timgorin.herokuapp.com/)

## Install

Prerequisites: [Python](https://www.python.org/), [SQLite](https://www.sqlite.org/), [pip](https://pip.pypa.io/), [virtualenv](https://virtualenv.readthedocs.org/), [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/), [Git](http://git-scm.com/).

Your `~/.bash_profile`:

```
# Paths
export PATH=/usr/local/bin:$PATH

# Virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh

# Tim Gorin
export TIMGORIN_SECRET_KEY='...'
```

Replace `...` with a [Django Secret Key](http://www.miniwebtool.com/django-secret-key-generator/) and restart Terminal.

Download and install:

```
mkdir -p ~/Sites/ && cd ~/Sites/
git clone git@github.com:richardcornish/timgorin.git
mkvirtualenv timgorin
cd timgorin/
pip install -r requirements.txt
cd timgorin/
python manage.py migrate
python manage.py loaddata timgorin/fixtures/*
python manage.py createsuperuser
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000). Kill with `Ctrl+C`.

Setting a virtualenv default directory is usually a good idea:

```
setvirtualenvproject $WORKON_HOME/timgorin/ ~/Sites/timgorin/timgorin/
```

## Scrape

To run the spider to scrape the website:

```
cd scraper/
scrapy crawl eslcafe
```

## Search

Elasticsearch is required to update the search index. Assuming [Homebrew](http://brew.sh/) is installed:

1. `brew install caskroom/cask/brew-cask`
2. `brew install Caskroom/cask/java`
3. `brew install elasticsearch`
4. `elasticsearch --config=/usr/local/opt/elasticsearch/config/elasticsearch.yml`
5. `python manage.py rebuild_index` (or `python manage.py update_index` subsequent times).

## Deploy

The code is set up to deploy to [Heroku](https://www.heroku.com/), and as such requires the Heroku Toolbelt:

- [Heroku Toolbelt](https://toolbelt.heroku.com/)

Heroku add-ons I installed:

- [Heroku Postgres](https://addons.heroku.com/heroku-postgresql)
- [Heroku PG Backups](https://addons.heroku.com/pgbackups)
- [Heroku Scheduler](https://addons.heroku.com/scheduler)
- [SearchBox Elasticsearch](https://addons.heroku.com/searchbox)

Heroku requires some [environment variables](https://devcenter.heroku.com/articles/config-vars):

```
heroku login
heroku create
heroku config:set TIMGORIN_SECRET_KEY='...'
heroku config:set DEBUG=''
heroku config:set WEB_CONCURRENCY='2'
heroku addons:add heroku-postgresql
heroku addons:add pgbackups
heroku addons:add scheduler
heroku addons:add searchbox
git push heroku master
heroku run python timgorin/manage.py migrate
heroku run python timgorin/manage.py loaddata timgorin/fixtures/*
heroku run python timgorin/manage.py createsuperuser
heroku open
```

Future deploys:

```
git push heroku master
```

After installation you can then run the commands straight to Heroku:

```
heroku run '(cd timgorin/scraper/ && scrapy crawl eslcafe)'
heroku run python timgorin/manage.py rebuild_index
```

But you will more likely want to run the [Scheduler](https://scheduler.heroku.com/dashboard), which runs these tasks every day to scrape the website and update the search index:

- `(cd scraper/ && scrapy crawl eslcafe)`
- `python timgorin/manage.py update_index`

You might need to edit the [SearchBox settings](https://dashboard.searchly.com/6886/indices) on your Heroku dashboard to manually register your SearchBox API key and your search index's name.

## Resources

Resources that helped me:

- [hk0weather](https://github.com/sammyfung/hk0weather) Hong Kong weather data project by [Sammy Fung](http://sammy.hk/)
- [Python, Web scraping and content management: Scrapy and Django](http://www.slideshare.net/sammyfung/python-web-scraping-and-content-management-scrapy-and-django)
- [Open Data, Open Government](http://www.slideshare.net/sammyfung/hk0weather-barcamp)
- New Coder "[Web scraper](http://newcoder.io/scrape/)" tutorial by [Lynn Root](http://www.roguelynn.com/)
- [Getting started with Django on Heroku](https://devcenter.heroku.com/articles/getting-started-with-django) by Heroku
