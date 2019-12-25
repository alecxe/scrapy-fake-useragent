import pytest
from scrapy import Request
from scrapy.http import Response

from scrapy.spiders import Spider
from scrapy.utils.test import get_crawler
from twisted.internet.error import DNSLookupError

from scrapy_fake_useragent.middleware import RetryUserAgentMiddleware


@pytest.fixture
def retry_middleware_response(request):
    """
    Fixture to simplify creating a crawler
    with an activated middleware and going through
    the request-response cycle.

    Executes process_response() method of the middleware.
    """
    settings, status = request.param

    crawler = get_crawler(Spider, settings_dict=settings)
    spider = crawler._create_spider('foo')
    mw = RetryUserAgentMiddleware.from_crawler(crawler)

    req = Request('http://www.scrapytest.org/')
    rsp = Response(req.url, body=b'', status=status)

    yield mw.process_response(req, rsp, spider)


@pytest.fixture
def retry_middleware_exception(request):
    """
    Fixture to simplify creating a crawler
    with an activated retry middleware and going through
    the request-response cycle.

    Executes process_exception() method of the middleware.
    """
    settings, exception = request.param

    crawler = get_crawler(Spider, settings_dict=settings)
    spider = crawler._create_spider('foo')
    mw = RetryUserAgentMiddleware.from_crawler(crawler)

    req = Request('http://www.scrapytest.org/')

    yield mw.process_exception(req, exception, spider)


@pytest.mark.parametrize(
    'retry_middleware_response',
    (({'FAKEUSERAGENT_FALLBACK': 'firefox'}, 503), ),
    indirect=True
)
def test_random_ua_set_on_response(retry_middleware_response):
    assert 'User-Agent' in retry_middleware_response.headers


@pytest.mark.parametrize(
    'retry_middleware_exception',
    (({'FAKEUSERAGENT_FALLBACK': 'firefox'},
      DNSLookupError('Test exception')), ),
    indirect=True
)
def test_random_ua_set_on_exception(retry_middleware_exception):
    assert 'User-Agent' in retry_middleware_exception.headers
