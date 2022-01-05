SECRET_KEY = 'not-secret-anymore'

TIME_ZONE = 'UTC'
USE_TZ = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}

ROOT_URLCONF = 'tests.urls'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'rest_framework',
    'drf_jsonmask',
    'tests',
]

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
