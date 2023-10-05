import logging

from celery.schedules import crontab

logger = logging.getLogger()

PYTHONPATH = $PYTHONPATH

# database configurations (do not modify)

RATELIMIT_STORAGE_URI = $SUPERSET_CACHE_REDIS_URL
SQLALCHEMY_DATABASE_URI = $SQLALCHEMY_DATABASE_URI
SUPERSET_CACHE_REDIS_URL = $SUPERSET_CACHE_REDIS_URL

CACHE_CONFIG = {
    "CACHE_TYPE": "RedisCache",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "superset_",
    "CACHE_REDIS_HOST": $REDIS_HOST,
    "CACHE_REDIS_PORT": $REDIS_PORT,
    "CACHE_REDIS_DB": 0,
    'CACHE_REDIS_URL': $REDIS_URL 
}
DATA_CACHE_CONFIG = CACHE_CONFIG

#redis-cli -u redis://default:JcOpyrs7uZlse7cCzlDu@containers-us-west-198.railway.app:7283
class CeleryConfig(object):
    BROKER_URL = f$SUPERSET_CACHE_REDIS_URL + "/1"
    CELERY_IMPORTS= ("superset.sql_lab",)
    CELERY_RESULT_BACKEND = f$SUPERSET_CACHE_REDIS_URL + "/0"
    CELERY_ANNOTATIONS = {'tasks.add': {'rate_limit': '10/s'}}

CELERY_CONFIG = CeleryConfig

# database engine specific ironment variables
# change the below if you prefer another database engine
#POSTGRES_DB = $POSTGRES_DB
#POSTGRES_USER = $POSTGRES_USER
#POSTGRES_PASSWORD = $POSTGRES_PASSWORD
#MYSQL_DATABASE=superset
#MYSQL_USER=superset
#MYSQL_PASSWORD=superset
#MYSQL_RANDOM_ROOT_PASSWORD=yes

# Add the mapped in /app/pythonpath_docker which allows devs to override stuff
REDIS_HOST = $REDIS_HOST
REDIS_PORT = $REDIS_PORT

SUPERSET_ENV = $SUPERSET_ENV
SUPERSET_LOAD_EXAMPLES = $SUPERSET_LOAD_EXAMPLES
SUPERSET_SECRET_KEY = $SUPERSET_SECRET_KEY
# CYPRESS_CONFIG = $CYPRESS_CONFIG
SUPERSET_PORT = $SUPERSET_PORT