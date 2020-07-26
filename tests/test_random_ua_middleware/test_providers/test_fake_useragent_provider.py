import pytest


@pytest.mark.parametrize(
    'middleware_request',
    ({'FAKE_USERAGENT_RANDOM_UA_TYPE': 'trash',
      'FAKEUSERAGENT_FALLBACK': 'Mozilla/5.0 (Android; Mobile; rv:40.0)',
      'RANDOM_UA_PER_PROXY': True},),
    indirect=True
)
def test_fua_bad_type_ua_set(middleware_request):
    assert middleware_request.headers == {
        b'User-Agent': [b'Mozilla/5.0 (Android; Mobile; rv:40.0)']
    }
