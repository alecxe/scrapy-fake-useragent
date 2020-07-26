import pytest


@pytest.mark.parametrize(
    'middleware_request',
    ({'FAKEUSERAGENT_PROVIDERS': ['scrapy_fake_useragent.providers.FixedUserAgentProvider'],
      'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0)'},),
    indirect=True
)
def test_fixed_ua_set(middleware_request):
    assert middleware_request.headers == {
        b'User-Agent': [b'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0)']
    }
