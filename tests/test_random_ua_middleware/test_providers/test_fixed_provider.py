import pytest


@pytest.mark.parametrize(
    'middleware_request',
    ({'FAKEUSERAGENT_PROVIDERS': ['scrapy_fake_useragent.providers.FixedUserAgentProvider'],
      'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'},),
    indirect=True
)
def test_fixed_ua_set(middleware_request):
    assert 'User-Agent' in middleware_request.headers
