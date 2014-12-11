[![GitHub version](https://badge.fury.io/gh/alecxe%2Fscrapy-fake-useragent.svg)](http://badge.fury.io/gh/alecxe%2Fscrapy-fake-useragent)
[![Requirements Status](https://requires.io/github/alecxe/scrapy-fake-useragent/requirements.svg?branch=master)](https://requires.io/github/alecxe/scrapy-fake-useragent/requirements/?branch=master)

scrapy-fake-useragent
=====================

Random User-Agent middleware based on [fake-useragent](https://pypi.python.org/pypi/fake-useragent). 
It picks up `User-Agent` strings based on [usage statistics](http://www.w3schools.com/browsers/browsers_stats.asp) from a [real world database](http://useragentstring.com/).

Configuration
-------------

Turn off the built-in `UserAgentMiddleware` and add `FakeUserAgentMiddleware`:

    DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
        'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    }
