web: gunicorn jobboardscraper.wsgi --pythonpath jobboardscraper --log-file -
worker: celery --app=jobboardscraper beat --loglevel=INFO