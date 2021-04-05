import multiprocessing

workers = multiprocessing.cpu_count()
threads = 2
bind = ':8000'
worker_class = 'gevent'
pidfile = 'gunicorn/gunicorn.pid'
accesslog = 'gunicorn/gunicorn_access.log'
errorlog = 'gunicorn/gunicorn_error.log'