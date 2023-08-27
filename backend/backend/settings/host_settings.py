from decouple import config, Csv

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

CORS_ORIGIN_ALLOW_ALL = True
