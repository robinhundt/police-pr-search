#!/bin/sh
sleep 1
gunicorn \
  --bind 0.0.0.0:8000 \
  --workers=4 \
  --log-level debug \
  wsgi:app
