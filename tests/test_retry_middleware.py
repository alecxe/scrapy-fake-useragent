import pytest
from twisted.internet.error import DNSLookupError


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
