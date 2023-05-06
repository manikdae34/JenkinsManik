#!/bin/sh

ssh apps@27.147.180.32 <<EOF
  cd JenkinsManik
  git pull
  source /opt/envs/JenkinsManik/bin/activate
  pip install -r requirements.txt
  ./manage.py makemigrations
  ./manage.py migrate  --run-syncdb
  sudo service gunicorn restart
  sudo service nginx restart
  exit
EOF
