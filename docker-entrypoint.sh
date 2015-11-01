#!/bin/bash
set -e

service carbon-cache start
/opt/graphite/bin/run-graphite-devel-server.py /opt/graphite/

exec "$@"
