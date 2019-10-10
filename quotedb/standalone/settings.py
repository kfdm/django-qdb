import pathlib
import environ

from django.urls import reverse_lazy

BASE_DIR = pathlib.Path(__file__).parent.parent.parent

env = environ.Env()
try:
    environ.Env.read_env(env("DJANGO_ENV_FILE"))
except FileNotFoundError:
    pass

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["*"])

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "django_filters",
    "quotedb.standalone",
    "quotedb",
    "debug_toolbar",
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "quotedb.standalone.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "quotedb.standalone.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DEFAULT_DATABASE = BASE_DIR / "db.sqlite3"
DATABASES = {"default": env.db(default="sqlite://%s" % DEFAULT_DATABASE)}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = env("TIMEZONE", default="UTC")

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_DEFAULT = pathlib.Path.home() / ".cache" / "quotedb"
STATIC_URL = "/static/"
STATIC_ROOT = env("STATIC_ROOT", default=STATIC_DEFAULT)

LOGIN_REDIRECT_URL = reverse_lazy("quotes:quote-list")

try:
    assert DEBUG is True
    import debug_toolbar  # NOQA
except (ImportError, AssertionError):
    MIDDLEWARE.remove("debug_toolbar.middleware.DebugToolbarMiddleware")
    INSTALLED_APPS.remove("debug_toolbar")
else:
    INTERNAL_IPS = ["127.0.0.1"]

try:
    import whitenoise  # NOQA
except ImportError:
    MIDDLEWARE.remove("whitenoise.middleware.WhiteNoiseMiddleware")
else:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
