.. image:: https://badge.fury.io/py/scrapy-fake-useragent.svg
     :target: http://badge.fury.io/py/scrapy-fake-useragent
     :alt: PyPI version

.. image:: https://requires.io/github/alecxe/scrapy-fake-useragent/requirements.svg?branch=master
     :target: https://requires.io/github/alecxe/scrapy-fake-useragent/requirements/?branch=master
     :alt: Requirements Status

scrapy-fake-useragent
=====================

Random User-Agent middleware based on
`fake-useragent <https://pypi.python.org/pypi/fake-useragent>`__. It
picks up ``User-Agent`` strings based on `usage
statistics <http://www.w3schools.com/browsers/browsers_stats.asp>`__
from a `real world database <http://useragentstring.com/>`__.

Installation
-------------

The simplest way is to install it via `pip`:

    pip install scrapy-fake-useragent

Configuration
-------------

Turn off the built-in ``UserAgentMiddleware`` and add
``RandomUserAgentMiddleware``.

In Scrapy >=1.0:

.. code:: python

    DOWNLOADER_MIDDLEWARES = {
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    }

In Scrapy <1.0:

.. code:: python

    DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
        'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    }

Configuring User-Agent type
---------------------------

There's a configuration parameter ``RANDOM_UA_TYPE`` defaulting to ``random`` which is passed verbatim to the fake-user-agent. Therefore you can set it to say ``firefox`` to mimic only firefox browsers. Most useful though would be to use ``desktop`` or ``mobile`` values to send desktop or mobile strings respectively.

Usage with `scrapy-proxies`
---------------------------

To use with middlewares of random proxy such as `scrapy-proxies <https://github.com/aivarsk/scrapy-proxies>`_, you need:

1. set ``RANDOM_UA_PER_PROXY`` to True to allow switch per proxy

2. set priority of ``RandomUserAgentMiddleware`` to be greater than ``scrapy-proxies``, so that proxy is set before handle UA


.. |GitHub version| image:: https://badge.fury.io/gh/alecxe%2Fscrapy-fake-useragent.svg
   :target: http://badge.fury.io/gh/alecxe%2Fscrapy-fake-useragent
.. |Requirements Status| image:: https://requires.io/github/alecxe/scrapy-fake-useragent/requirements.svg?branch=master
   :target: https://requires.io/github/alecxe/scrapy-fake-useragent/requirements/?branch=master

Configuring Fake-UserAgent fallback
----------------------------------

There's a configuration parameter ``FAKEUSERAGENT_FALLBACK`` defaulting to
``None``. You can set it to a string value, for example ``Mozilla`` or
``Your favorite browser``, this configuration can completely disable any
annoying exception.
