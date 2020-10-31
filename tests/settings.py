SECRET_KEY = 'not-secret-anymore'

TIME_ZONE = 'UTC'

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
