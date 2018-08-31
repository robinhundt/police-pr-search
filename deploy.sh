#!/bin/sh
sleep 1
gunicorn \
  --bind 0.0.0.0:8000 \
  --workers=2 \
  --worker-class=gevent \
  --log-level debug \
  wsgi
