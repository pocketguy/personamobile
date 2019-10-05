# see https://pythonspeed.com/articles/gunicorn-in-docker/
workers = 2
threads = 4
accesslog = "-"
errorlog = "-"
worker_tmp_dir = "/dev/shm"
worker_class = "gthread"
bind = ["0.0.0.0:80"]
