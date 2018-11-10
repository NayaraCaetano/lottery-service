#!/bin/bash
set -e

if [ "$1" == "run" ]; then
  if [ "$DEBUG" != 'True' ] && [ "$DEBUG" != 'true' ]; then
      python manage.py collectstatic -v 2 --noinput --no-color
  else
      export PYTHONDONTWRITEBYTECODE=1
  fi

  # Migrations
  python manage.py migrate --no-color --no-input --verbosity 2

  if [ "$DEBUG" = 'True' ] || [ "$DEBUG" = 'true' ]; then
      python manage.py runserver 0.0.0.0:8000
  else
      gunicorn "lottery_service.wsgi:application" \
          --bind 0.0.0.0:$PORT
  fi

else
    echo "Command not found '$1'"
    exit 1
fi