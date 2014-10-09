# Job board scraper

This code scrapes a job board daily with [Scrapy](http://scrapy.org/) and integrates it into a [Django](https://www.djangoproject.com/) website. The website is hosted on [Heroku](https://www.heroku.com/).

Deployed website:

- [http://timgorin.herokuapp.com](http://timgorin.herokuapp.com/)

Heroku add-ons I used:

- [Heroku Scheduler](https://addons.heroku.com/scheduler)
- [Heroku Postgres](https://addons.heroku.com/heroku-postgresql)

Scrapy requires a Scrapy project to be created, changing into its project directory, and then running the spider. Therefore, the task for the Scheduler is `(cd scraper && scrapy crawl eslcafe)`.

Resources that helped me:

- [hk0weather](https://github.com/sammyfung/hk0weather) Hong Kong weather data project by [Sammy Fung](http://sammy.hk/)
- [Python, Web scraping and content management: Scrapy and Django](http://www.slideshare.net/sammyfung/python-web-scraping-and-content-management-scrapy-and-django)
- [Open Data, Open Government](http://www.slideshare.net/sammyfung/hk0weather-barcamp)
- New Coder "[Web scraper](http://newcoder.io/scrape/)" tutorial by [Lynn Root](http://www.roguelynn.com/)
- [Getting started with Django on Heroku](https://devcenter.heroku.com/articles/getting-started-with-django)
