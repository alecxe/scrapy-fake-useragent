.. image:: https://travis-ci.org/alecxe/scrapy-fake-useragent.svg?branch=master
    :target: https://travis-ci.org/alecxe/scrapy-fake-useragent

.. image:: https://codecov.io/gh/alecxe/scrapy-fake-useragent/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/alecxe/scrapy-fake-useragent

.. image:: https://img.shields.io/pypi/pyversions/scrapy-fake-useragent.svg
     :target: https://pypi.python.org/pypi/scrapy-fake-useragent
     :alt: PyPI version

.. image:: https://badge.fury.io/py/scrapy-fake-useragent.svg
     :target: http://badge.fury.io/py/scrapy-fake-useragent
     :alt: PyPI version

.. image:: https://requires.io/github/alecxe/scrapy-fake-useragent/requirements.svg?branch=master
     :target: https://requires.io/github/alecxe/scrapy-fake-useragent/requirements/?branch=master
     :alt: Requirements Status


scrapy-fake-useragent
=====================

Random User-Agent middleware for Scrapy scraping framework based on
`fake-useragent <https://pypi.python.org/pypi/fake-useragent>`__, which picks up ``User-Agent`` strings 
based on `usage statistics <http://www.w3schools.com/browsers/browsers_stats.asp>`__
from a `real world database <http://useragentstring.com/>`__ and 
`fake-useragent <https://faker.readthedocs.io/en/stable/providers/faker.providers.user_agent.html>`__ which generates
random ``User-Agent`` strings from a combination of possibilities. It also has the possibility of extending the
capabilities of the middleware, by adding your own providers.

Installation
-------------

The simplest way is to install it via `pip`:

    pip install scrapy-fake-useragent

Configuration
-------------

Turn off the built-in ``UserAgentMiddleware`` and ``RetryMiddleware`` and add
``RandomUserAgentMiddleware`` and ``RetryUserAgentMiddleware``.

In Scrapy >=1.0:

.. code:: python

    DOWNLOADER_MIDDLEWARES = {
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
        'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
        'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
    }

In Scrapy <1.0:

.. code:: python

    DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
        'scrapy.contrib.downloadermiddleware.retry.RetryMiddleware': None,
        'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
        'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
    }

Enabling providers
---------------------------

Each provider is enabled individually, and used in the order they are defined.
In case a provider fails execute (it can happen to fake-useragent because of it's dependancy
with an online service), the next one will be used.

In ``settings.py``:

.. code:: python

    FAKEUSERAGENT_PROVIDERS = [
        'scrapy_fake_useragent.providers.FakeUserAgent',
        'scrapy_fake_useragent.providers.Faker',
        'scrapy_fake_useragent.providers.FixedUserAgent',
        'mypackage.providers.CustomProvider'
    ]


Configuring User-Agent type
---------------------------

This middleware comes with two already pre-implemented User-Agent providers.
The configuration for these providers is independant and also specific for the underlying libraries.
For understanding which are the values you can set for each provider, refer to the libraries cited before.

### fake-useragent
Parameter: ``FAKE_USERAGENT_RANDOM_UA_TYPE`` defaulting to ``random``
Other options, as example: 
 * ``firefox`` to mimic only firefox browsers
 * ``desktop`` or ``mobile`` values to send desktop or mobile strings respectively.

You can also set the ``FAKEUSERAGENT_FALLBACK`` option, which is a ``fake-useragent`` specific fallback.
What it does is, if the selected ``FAKE_USERAGENT_RANDOM_UA_TYPE`` fails to retrieve a UA, it will use
the type set in ``FAKEUSERAGENT_FALLBACK``.

### Faker
Parameter: ``FAKER_RANDOM_UA_TYPE`` defaulting to ``user_agent`` which is the way of selecting totally random User-Agents values.
Other options, as example:
 * ``chrome``
 * ``firefox``

### FixedUserAgent

It also comes with a fixed provider (only provides one user agent), reusing the Scrapy's config ``USER_AGENT``.

Usage with `scrapy-proxies`
---------------------------

To use with middlewares of random proxy such as `scrapy-proxies <https://github.com/aivarsk/scrapy-proxies>`_, you need:

1. set ``RANDOM_UA_PER_PROXY`` to True to allow switch per proxy

2. set priority of ``RandomUserAgentMiddleware`` to be greater than ``scrapy-proxies``, so that proxy is set before handle UA


.. |GitHub version| image:: https://badge.fury.io/gh/alecxe%2Fscrapy-fake-useragent.svg
   :target: http://badge.fury.io/gh/alecxe%2Fscrapy-fake-useragent
.. |Requirements Status| image:: https://requires.io/github/alecxe/scrapy-fake-useragent/requirements.svg?branch=master
   :target: https://requires.io/github/alecxe/scrapy-fake-useragent/requirements/?branch=master
