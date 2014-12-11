scrapy-fake-useragent
=====================

Random User-Agent middleware based on [fake-useragent](https://pypi.python.org/pypi/fake-useragent)

Configuration
-------------

Turn off the built-in `UserAgentMiddleware` and add `FakeUserAgentMiddleware`:

    DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
        'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    }
