web: gunicorn jobboardscraper.wsgi --pythonpath jobboardscraper --log-file -
worker: celery worker --app=jobboardscraper.celery:app beat --loglevel=INFO