from setuptools import find_packages, setup

from quotedb.version import __version__

setup(
    name="django-qdb",
    version=__version__,
    packages=find_packages(exclude=["test"]),
    include_package_data=True,
    license="MIT License",
    description="A simple quote database",
    url="https://github.com/kfdm/django-qdb",
    author="Paul Traylor",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=[
        "djangorestframework",
        "django-filter"
    ],
    extras_require={
        "standalone": [
            "django==2.0.6",
            "dj_database_url",
            "envdir",
            "prometheus_client",
            "raven",
            "social-auth-app-django==2.1.0",
            "gunicorn",
        ],
        "postgres": ["psycopg2"],
    },
    entry_points={
        "console_scripts": ["quotedb = quotedb.standalone.manage:main[standalone]"],
        "powerplug.apps": ["quotes = quotedb"],
        "powerplug.urls": ["quotes = quotedb.urls"],
        "powerplug.rest": ["quotes = quotedb.rest:QuoteViewSet"],
    },
)
