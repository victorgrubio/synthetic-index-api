#!/bin/sh

cd app
echo "Waiting for postgres..."

while ! nc -z $SQL_HOST $SQL_PORT; do
    sleep 0.1
done

echo "Database started"
gunicorn --worker-class=gevent --workers 1 --bind 0.0.0.0:${API_PORT} wsgi:app
