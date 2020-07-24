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


# Test FakeUserAgent with an invalid UA type set. Should still use the default
@pytest.mark.parametrize(
    'middleware_request',
    ({'FAKEUSERAGENT_FALLBACK': 'firefox',
      'FAKE_USERAGENT_RANDOM_UA_TYPE': 'trash',
      'RANDOM_UA_PER_PROXY': True}, ),
    indirect=True
)
def test_fua_bad_type_ua_set(middleware_request):
    assert 'User-Agent' in middleware_request.headers


# Test faker provider working alone
@pytest.mark.parametrize(
    'middleware_request',
    ({'FAKEUSERAGENT_PROVIDERS': ['scrapy_fake_useragent.providers.FakerProvider']}, ),
    indirect=True
)
def test_faker_ua_set(middleware_request):
    assert 'User-Agent' in middleware_request.headers


# Test FakerProvider with an invalid UA type set. Should still use the default
@pytest.mark.parametrize(
    'middleware_request',
    ({'FAKEUSERAGENT_PROVIDERS': ['scrapy_fake_useragent.providers.FakerProvider'],
      'FAKER_RANDOM_UA_TYPE': 'trash'}, ),
    indirect=True
)
def test_faker_bad_type_ua_set(middleware_request):
    assert 'User-Agent' in middleware_request.headers


@pytest.mark.parametrize(
    'middleware_request',
    ({'FAKEUSERAGENT_PROVIDERS': ['scrapy_fake_useragent.providers.FixedUserAgentProvider'],
      'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}, ),
    indirect=True
)
def test_fixed_ua_set(middleware_request):
    assert 'User-Agent' in middleware_request.headers
