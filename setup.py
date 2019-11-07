from setuptools import setup, find_packages
from quotedb.version import __version__

setup(
    name='django-qdb',
    version=__version__,
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    license="MIT License",
    description="A simple quote database",
    url="https://github.com/kfdm/django-quotedb",
    author="Paul Traylor",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    install_requires=["djangorestframework", "django-filter>=2.0.0"],
    entry_points={
        "console_scripts": ["quotedb = quotedb.standalone.manage:main"],
        "powerplug.apps": ["quotes = quotedb"],
        "powerplug.urls": ["quotes = quotedb.urls"],
        "powerplug.rest": ["quotes = quotedb.rest:QuoteViewSet"],
    },
)
