import pytest


@pytest.mark.parametrize(
    'middleware_request',
    ({'FAKEUSERAGENT_PROVIDERS': ['scrapy_fake_useragent.providers.FakerProvider',
                                  'scrapy_fake_useragent.providers.FixedUserAgentProvider']},),
    indirect=True
)
def test_faker_ua_set(middleware_request):
    """Test faker provider working alone."""
    assert 'User-Agent' in middleware_request.headers

    # non-default UA used
    assert 'Scrapy' not in str(middleware_request.headers['User-Agent'])


@pytest.mark.parametrize(
    'middleware_request',
    ({'FAKEUSERAGENT_PROVIDERS': ['scrapy_fake_useragent.providers.FakerProvider'],
      'FAKER_RANDOM_UA_TYPE': 'trash'},),
    indirect=True
)
def test_faker_bad_type_ua_set(middleware_request):
    """Test FakerProvider with an invalid UA type set. Should still use the default."""
    assert 'User-Agent' in middleware_request.headers
