SECRET_KEY = 'UNSAFE_DEFAULT'

TIME_ZONE = 'GMT'

#DOCUMENTATION_URL = "http://graphite.readthedocs.org/"

# Logging
#LOG_RENDERING_PERFORMANCE = True
#LOG_CACHE_PERFORMANCE = True
#LOG_METRIC_ACCESS = True

# Enable full debug page display on exceptions (Internal Server Error pages)
DEBUG = True

# If using RRD files and rrdcached, set to the address or socket of the daemon
#FLUSHRRDCACHED = 'unix:/var/run/rrdcached.sock'

# Change only GRAPHITE_ROOT if your install is merely shifted from /opt/graphite
# to somewhere else
#GRAPHITE_ROOT = '/opt/graphite'

# Most installs done outside of a separate tree such as /opt/graphite will only
# need to change these three settings. Note that the default settings for each
# of these is relative to GRAPHITE_ROOT
#CONF_DIR = '/opt/graphite/conf'
#STORAGE_DIR = '/opt/graphite/storage'
#CONTENT_DIR = '/opt/graphite/webapp/content'

# To further or fully customize the paths, modify the following. Note that the
# default settings for each of these are relative to CONF_DIR and STORAGE_DIR
#
## Webapp config files
#DASHBOARD_CONF = '/opt/graphite/conf/dashboard.conf'
#GRAPHTEMPLATES_CONF = '/opt/graphite/conf/graphTemplates.conf'

## Data directories
# NOTE: If any directory is unreadable in DATA_DIRS it will break metric browsing
#WHISPER_DIR = '/opt/graphite/storage/whisper'
#RRD_DIR = '/opt/graphite/storage/rrd'
#DATA_DIRS = [WHISPER_DIR, RRD_DIR] # Default: set from the above variables
#LOG_DIR = '/opt/graphite/storage/log/webapp'
#INDEX_FILE = '/opt/graphite/storage/index'  # Search index file
