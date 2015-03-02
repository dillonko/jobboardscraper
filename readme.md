# Job board scraper

This code scrapes a job board with [Scrapy](http://scrapy.org/) every day and integrates it into a [Django](https://www.djangoproject.com/) website with an [Elasticsearch](http://www.elasticsearch.org/) search index and a [PostgreSQL](http://www.postgresql.org/) database. The website is hosted on [Heroku](https://www.heroku.com/).

The deployed website: [http://timgorin.herokuapp.com](http://timgorin.herokuapp.com/)

## Installation

Prerequisites:

- [Python](https://www.python.org/)
- [SQLite](http://www.sqlite.org/)
- [pip](https://pip.pypa.io/)
- [virtualenv](http://virtualenv.readthedocs.org/)
- [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/)
- [Git](http://git-scm.com/)

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
add2virtualenv timgorin/
cd timgorin/
python manage.py migrate
python manage.py loaddata fixtures/*
python manage.py createsuperuser
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000). Kill with `Ctrl+C`.

Setting a virtualenv default directory is usually a good idea:

```
setvirtualenvproject $WORKON_HOME/timgorin/ ~/Sites/timgorin/timgorin/
```

Start to work again:

```
workon timgorin
deactivate
```

Future database changes:

```
python manage.py makemigrations
python manage.py migrate
```

## Scrape

To run the spider to scrape the website:

```
workon timgorin
cd ../scraper/
scrapy crawl eslcafe
deactivate
```

## Search

Elasticsearch (and thus Java) is required to update the search index. Assuming [Homebrew](http://brew.sh/) is installed:

1. Install [Java JDK and Java JRE](http://www.oracle.com/technetwork/java/javase/downloads/index.html)
2. `brew install elasticsearch`
3. `elasticsearch --config=/usr/local/opt/elasticsearch/config/elasticsearch.yml`
4. `python manage.py rebuild_index` (or `python manage.py update_index` subsequent times).

## Deployment

The code is set up to deploy to [Heroku](https://www.heroku.com/).

Heroku add-ons I installed:

- [Heroku Postgres](https://addons.heroku.com/heroku-postgresql)
- [Heroku PG Backups](https://addons.heroku.com/pgbackups)
- [Heroku Scheduler](https://addons.heroku.com/scheduler)
- [SearchBox Elasticsearch](https://addons.heroku.com/searchbox)

Heroku requires some [environment variables](https://devcenter.heroku.com/articles/config-vars):

```
heroku create
heroku config:set TIMGORIN_SECRET_KEY='...'
heroku config:set DJANGO_SETTINGS_MODULE='timgorin.settings'
heroku config:set DEBUG=''
heroku config:set WEB_CONCURRENCY='2'
heroku addons:add heroku-postgresql
heroku addons:add pgbackups
heroku addons:add scheduler
heroku addons:add searchbox
git push heroku master
heroku run python manage.py syncdb
heroku run python manage.py loaddata fixtures/*
heroku open
```

Future deploys:

Commit your files with Git.

```
git push heroku master
heroku run python manage.py migrate
```

After installation you can then run the commands straight to Heroku:

```
heroku run '(cd ../scraper/ && scrapy crawl eslcafe)'
heroku run python manage.py rebuild_index
```

Consult Heroku's "[Getting started with Django on Heroku](https://devcenter.heroku.com/articles/getting-started-with-django)" article on production installation.

You will more likely want to run the Scheduler, which needs to run these tasks every day to scrape the website and update the search index:

- `(cd ../scraper/ && scrapy crawl eslcafe)`
- `python manage.py update_index`

You might need to edit the [SearchBox settings](https://dashboard.searchly.com/6886/indices) on your Heroku dashboard to manually register your SearchBox API key and your search index's name.

## Resources

Resources that helped me:

- [hk0weather](https://github.com/sammyfung/hk0weather) Hong Kong weather data project by [Sammy Fung](http://sammy.hk/)
- [Python, Web scraping and content management: Scrapy and Django](http://www.slideshare.net/sammyfung/python-web-scraping-and-content-management-scrapy-and-django)
- [Open Data, Open Government](http://www.slideshare.net/sammyfung/hk0weather-barcamp)
- New Coder "[Web scraper](http://newcoder.io/scrape/)" tutorial by [Lynn Root](http://www.roguelynn.com/)
