.. image:: https://badge.fury.io/gh/alecxe%2Fscrapy-fake-useragent.svg
     :target: http://badge.fury.io/gh/alecxe%2Fscrapy-fake-useragent
     :alt: GitHub version

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

Configuration
-------------

Turn off the built-in ``UserAgentMiddleware`` and add
``RandomUserAgentMiddleware``:

::

    DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
        'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    }

.. |GitHub version| image:: https://badge.fury.io/gh/alecxe%2Fscrapy-fake-useragent.svg
   :target: http://badge.fury.io/gh/alecxe%2Fscrapy-fake-useragent
.. |Requirements Status| image:: https://requires.io/github/alecxe/scrapy-fake-useragent/requirements.svg?branch=master
   :target: https://requires.io/github/alecxe/scrapy-fake-useragent/requirements/?branch=master
