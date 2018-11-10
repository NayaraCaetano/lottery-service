#!/bin/bash
set -e

# Collect static files
if [ "$DEBUG" != 'True' ] && [ "$DEBUG" != 'true' ]; then
    python manage.py collectstatic -v 2 --noinput --no-color
else
    export PYTHONDONTWRITEBYTECODE=1
fi

# Migrations
python manage.py migrate --no-color --no-input --verbosity 2


if [ "$DEBUG" = 'True' ] || [ "$DEBUG" = 'true' ]; then
    exec python manage.py runserver 0.0.0.0:8000
else
    exec gunicorn "lottery_service.wsgi:application" \
        --bind 0.0.0.0:8000 \
        --name lottery_service
        --access-logfile - \
        --error-logfile - \
        --log-level debug \
        --capture-output True \
        --workers 2 \
        --threads 4 \
        --timeout 300
fi
