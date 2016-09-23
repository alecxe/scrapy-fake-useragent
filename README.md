# scrapy-fake-useragent

[![PyPI version](https://badge.fury.io/py/scrapy-fake-useragent.svg)](http://badge.fury.io/py/scrapy-fake-useragent)
[![Requirements Status](https://requires.io/github/alecxe/scrapy-fake-useragent/requirements.svg?branch=master)](https://requires.io/github/alecxe/scrapy-fake-useragent/requirements/?branch=master)

Random User-Agent middleware based on [fake-useragent]. It picks up `User-Agent` strings based on [usage statistics] from a [real world database].

## Configuration

Turn off the built-in `UserAgentMiddleware` and add `RandomUserAgentMiddleware`.

In Scrapy &gt;=1.0:

    DOWNLOADER_MIDDLEWARES = {
        'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
        'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    }

In Scrapy &lt;1.0:

    DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
        'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    }

## Usage with scrapy-proxies

To use with middlewares of random proxy such as [scrapy-proxies], you need:

1.  set `RANDOM_UA_PER_PROXY` to True to allow switch per proxy
2.  set priority of `RandomUserAgentMiddleware` to be greater than `scrapy-proxies`, so that proxy is set before handle UA

  [fake-useragent]: https://pypi.python.org/pypi/fake-useragent
  [usage statistics]: http://www.w3schools.com/browsers/browsers_stats.asp
  [real world database]: http://useragentstring.com/
  [scrapy-proxies]: https://github.com/aivarsk/scrapy-proxies