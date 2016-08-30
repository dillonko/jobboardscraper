web: gunicorn jobboardscraper.wsgi --pythonpath jobboardscraper --log-file -
worker: celery worker --app=jobboardscraper.celery_app:app beat --loglevel=INFO