import logging

from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.utils.response import response_status_message
from scrapy.utils.misc import load_object

logger = logging.getLogger(__name__)

class RandomUserAgentBase:
    def __init__(self, crawler):
        self._ua_provider = self._get_provider(crawler)
        self._per_proxy = crawler.settings.get('RANDOM_UA_PER_PROXY', False)
        self._proxy2ua = {}

    def _get_provider(self, crawler):
        self.providers_paths = crawler.setting.get('FAKEUSERAGENT_PROVIDERS', None)

        # To keep compatibility if the user didn't set a provider, fake-useragent will be used
        if not self.providers_paths:
            self.providers_paths = ['scrapy_fake_useragent.providers.FakeUserAgent']

        provider = None
        # We try to use any of the user agent providers specified in the config (priority order)
        for provider_path in self.providers_paths:
            try:
                provider = load_object(provider_path)(crawler)
                logger.debug('Using %s as the User-Agent provider', provider_path)
            except:    # Provider can throw anything
                logger.debug('Error on getting User-Agent provider: %s', provider_path)

        if not provider:
            # If none of them work, we use the FixedUserAgent provider:
            # (default provider that return a single useragent, like scrapy does, specified in USER_AGENT setting)
            provider = load_object('scrapy_fake_useragent.providers.FixedUserAgent')(crawler)

        return provider


class RandomUserAgentMiddleware(RandomUserAgentBase):
    def __init__(self, crawler):
        super().__init__(crawler)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        if self._per_proxy:
            proxy = request.meta.get('proxy')

            if proxy not in self._proxy2ua:
                self._proxy2ua[proxy] = self._ua_provider.get_random_ua()
                logger.debug('Assign User-Agent %s to Proxy %s'
                             % (self._proxy2ua[proxy], proxy))

            request.headers.setdefault('User-Agent', self._proxy2ua[proxy])
        else:
            request.headers.setdefault('User-Agent', self._ua_provider.get_random_ua())


class RetryUserAgentMiddleware(RetryMiddleware, RandomUserAgentBase):
    """
    Get random User-Agent set on request retry.
    Use this middleware in place of the built-in RetryMiddleware.
    """
    def __init__(self, crawler):
        RetryMiddleware.__init__(self, crawler.settings)
        RandomUserAgentBase.__init__(self, crawler)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_response(self, request, response, spider):
        if request.meta.get('dont_retry', False):
            return response

        if response.status in self.retry_http_codes:
            reason = response_status_message(response.status)
            request.headers['User-Agent'] = self._ua_provider.get_random_ua()
            return self._retry(request, reason, spider) or response

        return response

    def process_exception(self, request, exception, spider):
        if isinstance(exception, self.EXCEPTIONS_TO_RETRY) \
                and not request.meta.get('dont_retry', False):
            request.headers['User-Agent'] = self._ua_provider.get_random_ua()

            return self._retry(request, exception, spider)
