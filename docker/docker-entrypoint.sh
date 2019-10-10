#!/bin/sh

set -e

if [ "${1:0:1}" = '-' ]; then
	set -- quotedb "$@"
fi

case "$1" in
web)
  # Shortcut for launching a gunicorn worker
  shift
  set -- gunicorn "quotedb.standalone.wsgi:application" -b 0.0.0.0 "$@"
  ;;
esac

# Finally exec our command
exec "$@"
