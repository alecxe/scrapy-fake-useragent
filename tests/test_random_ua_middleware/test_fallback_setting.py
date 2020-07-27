import pytest


@pytest.mark.parametrize(
    'middleware_request',
    ({'FAKEUSERAGENT_FALLBACK': 'firefox'},),
    indirect=True
)
def test_random_ua_set(middleware_request):
    assert 'User-Agent' in middleware_request.headers


@pytest.mark.parametrize(
    'middleware_request',
    ({'FAKEUSERAGENT_FALLBACK': 'firefox',
      'RANDOM_UA_PER_PROXY': True},),
    indirect=True
)
def test_random_ua_per_proxy_set(middleware_request):
    assert 'User-Agent' in middleware_request.headers
