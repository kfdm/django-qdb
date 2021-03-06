from setuptools import setup, find_packages
from quotedb.version import __version__

setup(
    name='django-qdb',
    version=__version__,
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    license='MIT License',
    description='A simple quote database',
    url='https://github.com/kfdm/django-qdb',
    author='Paul Traylor',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        "djangorestframework",
        'django-filter>=2.0.0',
    ],
    entry_points={
        'powerplug.apps': ['quotes = quotedb'],
        'powerplug.urls': ['quotes = quotedb.urls'],
        'powerplug.rest': ['quotes = quotedb.rest:QuoteViewSet']
    },
)
