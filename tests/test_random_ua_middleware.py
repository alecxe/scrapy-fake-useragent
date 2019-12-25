import pytest
from scrapy import Request

from scrapy.spiders import Spider
from scrapy.utils.test import get_crawler

from scrapy_fake_useragent.middleware import RandomUserAgentMiddleware


@pytest.fixture
def middleware_request(request):
    crawler = get_crawler(Spider, settings_dict=request.param)
    spider = crawler._create_spider('foo')
    mw = RandomUserAgentMiddleware.from_crawler(crawler)

    req = Request('http://www.scrapytest.org/')

    mw.process_request(req, spider)

    yield req


@pytest.mark.parametrize(
    'middleware_request',
    ({'FAKEUSERAGENT_FALLBACK': 'firefox'}, ),
    indirect=True
)
def test_random_ua_set(middleware_request):
    assert 'User-Agent' in middleware_request.headers


@pytest.mark.parametrize(
    'middleware_request',
    ({'FAKEUSERAGENT_FALLBACK': 'firefox',
      'RANDOM_UA_PER_PROXY': True}, ),
    indirect=True
)
def test_random_ua_per_proxy_set(middleware_request):
    assert 'User-Agent' in middleware_request.headers
