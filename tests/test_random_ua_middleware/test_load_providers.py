import pytest
from scrapy import Request, Spider
from scrapy.utils.test import get_crawler

from scrapy_fake_useragent.middleware import RandomUserAgentMiddleware
from scrapy_fake_useragent.providers import FakerProvider


def test_cannot_load_providers(mocker):
    faker_provider_constructor = mocker.patch.object(FakerProvider, '__init__')
    faker_provider_constructor.side_effect = Exception("Cannot load Faker Provider")

    crawler = get_crawler(Spider, settings_dict={
        'FAKEUSERAGENT_PROVIDERS': ['scrapy_fake_useragent.providers.FakerProvider'],
        'USER_AGENT': 'Default User-Agent'}
                          )
    spider = crawler._create_spider('foo')
    mw = RandomUserAgentMiddleware.from_crawler(crawler)

    req = Request('http://www.scrapytest.org/')

    mw.process_request(req, spider)

    # check that we fell back to the default
    assert req.headers == {
        b'User-Agent': [b'Default User-Agent']
    }
