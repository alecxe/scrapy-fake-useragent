import fake_useragent
import pytest
from scrapy import Request
from scrapy.http import Response
from scrapy.spiders import Spider
from scrapy.utils.test import get_crawler

from scrapy_fake_useragent.middleware import RandomUserAgentMiddleware, RetryUserAgentMiddleware


@pytest.fixture(autouse=True)
def fake_useragent_always_loads(mocker):
    """Mock fake useragent to allow the fake useragent provider to load when testing."""
    fake_useragent_load = mocker.patch.object(fake_useragent.utils, 'load')
    fake_useragent_load.return_value = {
        'browsers': {'firefox': [
                'Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0'
            ]
        },
        'randomize': [
            'Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0'
        ]
    }


@pytest.fixture
def retry_middleware_response(fake_useragent_always_loads, request):
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
def retry_middleware_exception(fake_useragent_always_loads, request):
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


@pytest.fixture
def middleware_request(fake_useragent_always_loads, request):
    # middleware setup
    crawler = get_crawler(Spider, settings_dict=request.param)
    spider = crawler._create_spider('foo')
    mw = RandomUserAgentMiddleware.from_crawler(crawler)

    req = Request('http://www.scrapytest.org/')

    mw.process_request(req, spider)

    yield req
