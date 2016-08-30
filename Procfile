web: gunicorn jobboardscraper.wsgi --pythonpath jobboardscraper --log-file -
worker: celery --app=jobboardscraper --workdir=jobboardscraper worker -B