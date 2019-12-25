import unittest

from scrapy import Request

from scrapy.spiders import Spider
from scrapy.utils.test import get_crawler

from scrapy_fake_useragent.middleware import RandomUserAgentMiddleware


class RetryTest(unittest.TestCase):
    def setUp(self):
        self.crawler = get_crawler(Spider,
                                   settings_dict={
                                       'FAKEUSERAGENT_FALLBACK': 'firefox'
                                   })
        self.spider = self.crawler._create_spider('foo')
        self.mw = RandomUserAgentMiddleware.from_crawler(self.crawler)

    def test_random_ua_set(self):
        req = Request('http://www.scrapytest.org/')

        self.mw.process_request(req, self.spider)

        assert 'User-Agent' in req.headers
