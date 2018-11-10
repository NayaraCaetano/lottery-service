FROM python:3.7-alpine
MAINTAINER Nayara Caetano <nayara.caetanopinheiro@gmail.com>

ENV PYTHONUNBUFFERED=1

# Enable timezone support
ENV TZ=America/Sao_Paulo
RUN apk --no-cache add tzdata

# Install dependencies
COPY requirements.txt /
RUN apk add --no-cache \
        postgresql-dev && \
    apk add --no-cache --virtual .build-deps \
        gcc libc-dev \
        git && \
    pip install -r /requirements.txt && \
    apk del .build-deps

COPY entrypoint.sh /
ENTRYPOINT ["/bin/sh", "-c"]
CMD ["source /entrypoint.sh"]

# Add application data
WORKDIR /var/www
COPY . /var/www

# Create non-privileged user
RUN adduser -Ds /bin/sh loterry && \
    mkdir -p \
        /var/www/staticfiles \
        /var/log/loterry_service && \
    chown -R loterry:loterry \
        /var/www/staticfiles \
        /var/log/loterry_service
USER loterry
