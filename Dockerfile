FROM python:3.5.3-alpine
MAINTAINER kungfudiscomonkey@gmail.com

ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR off
ENV SECRET_KEY please-set-me

RUN mkdir -p /usr/src/app
COPY setup.py /usr/src/app/setup.py
COPY quotedb /usr/src/app/quotedb

WORKDIR /usr/src/app

RUN apk update && \
    apk add postgresql-libs && \
    apk add --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install -e .[standalone,postgres] --no-cache-dir && \
    apk --purge del .build-deps

EXPOSE 8000

RUN mkdir -p /usr/cache/app
ENV STATIC_ROOT /usr/cache/app
RUN quotedb collectstatic --noinput

CMD ["gunicorn", "quotedb.standalone.wsgi:application", "--bind", "0.0.0.0:8000"]
