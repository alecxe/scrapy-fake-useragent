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

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
     :target: https://github.com/alecxe/scrapy-fake-useragent/blob/master/LICENSE.txt
     :alt: Package license

scrapy-fake-useragent
=====================

Random User-Agent middleware for Scrapy scraping framework based on
`fake-useragent <https://pypi.python.org/pypi/fake-useragent>`__, which picks up ``User-Agent`` strings 
based on `usage statistics <http://www.w3schools.com/browsers/browsers_stats.asp>`__
from a `real world database <http://useragentstring.com/>`__, but also has the option to configure a generator
of fake UA strings, as a backup, powered by 
`Faker <https://faker.readthedocs.io/en/stable/providers/faker.providers.user_agent.html>`__.

It also has the possibility of extending the
capabilities of the middleware, by adding your own providers.

Changes
----------

Please see `CHANGELOG`_.

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

Recommended setting (1.3.0+):

.. code:: python

    FAKEUSERAGENT_PROVIDERS = [
        'scrapy_fake_useragent.providers.FakeUserAgentProvider',  # this is the first provider we'll try
        'scrapy_fake_useragent.providers.FakerProvider',  # if FakeUserAgentProvider fails, we'll use faker to generate a user-agent string for us
        'scrapy_fake_useragent.providers.FixedUserAgentProvider',  # fall back to USER_AGENT value
    ]
    USER_AGENT = '<your user agent string which you will fall back to if all other providers fail>'

----------------

Additional configuration information
====================================

Enabling providers
---------------------------

The package comes with a thin abstraction layer of User-Agent providers, which for purposes of backwards compatibility defaults to:

.. code:: python

    FAKEUSERAGENT_PROVIDERS = [
        'scrapy_fake_useragent.providers.FakeUserAgentProvider'
    ]

The package has also ``FakerProvider`` (powered by `Faker library <https://faker.readthedocs.io/>`__) and ``FixedUserAgentProvider`` implemented and available for use if needed.

Each provider is enabled individually, and used in the order they are defined.
In case a provider fails execute (for instance, it can `happen <https://github.com/hellysmile/fake-useragent/issues/99>`__ to fake-useragent because of it's dependency
with an online service), the next one will be used.

Example of what ``FAKEUSERAGENT_PROVIDERS`` setting may look like in your case:

.. code:: python

    FAKEUSERAGENT_PROVIDERS = [
        'scrapy_fake_useragent.providers.FakeUserAgentProvider',
        'scrapy_fake_useragent.providers.FakerProvider',
        'scrapy_fake_useragent.providers.FixedUserAgentProvider',
        'mypackage.providers.CustomProvider'
    ]


Configuring fake-useragent
---------------------------

Parameter: ``FAKE_USERAGENT_RANDOM_UA_TYPE`` defaulting to ``random``.

Other options, as example: 

* ``firefox`` to mimic only Firefox browsers
* ``msie`` to mimic Internet Explorer only
* etc.

You can also set the ``FAKEUSERAGENT_FALLBACK`` option, which is a ``fake-useragent`` specific fallback. For example:

.. code:: python

    FAKEUSERAGENT_FALLBACK = 'Mozilla/5.0 (Android; Mobile; rv:40.0)'

What it does is, if the selected ``FAKE_USERAGENT_RANDOM_UA_TYPE`` fails to retrieve a UA, it will use
the type set in ``FAKEUSERAGENT_FALLBACK``.

Configuring faker
---------------------------

Parameter: ``FAKER_RANDOM_UA_TYPE`` defaulting to ``user_agent`` which is the way of selecting totally random User-Agents values.
Other options, as example:

* ``chrome``
* ``firefox``

Configuring FixedUserAgent
---------------------------

It also comes with a fixed provider (only provides one user agent), reusing the Scrapy's default ``USER_AGENT`` setting value.

Usage with `scrapy-proxies`
---------------------------

To use with middlewares of random proxy such as `scrapy-proxies <https://github.com/aivarsk/scrapy-proxies>`_, you need:

1. set ``RANDOM_UA_PER_PROXY`` to True to allow switch per proxy

2. set priority of ``RandomUserAgentMiddleware`` to be greater than ``scrapy-proxies``, so that proxy is set before handle UA

License
----------

The package is under MIT license. Please see `LICENSE`_.

.. |GitHub version| image:: https://badge.fury.io/gh/alecxe%2Fscrapy-fake-useragent.svg
   :target: http://badge.fury.io/gh/alecxe%2Fscrapy-fake-useragent
.. |Requirements Status| image:: https://requires.io/github/alecxe/scrapy-fake-useragent/requirements.svg?branch=master
   :target: https://requires.io/github/alecxe/scrapy-fake-useragent/requirements/?branch=master
.. _LICENSE: https://github.com/alecxe/scrapy-fake-useragent/blob/master/LICENSE.txt
.. _CHANGELOG: https://github.com/alecxe/scrapy-fake-useragent/blob/master/CHANGELOG.rst
