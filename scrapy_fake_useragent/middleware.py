import logging
from fake_useragent import UserAgent

from scrapy import signals
from scrapy.downloadermiddlewares.retry import RetryMiddleware

logger = logging.getLogger(__name__)

class RandomUserAgentMiddleware(object):
    def __init__(self, crawler):
        super(RandomUserAgentMiddleware, self).__init__()

        fallback = crawler.settings.get('FAKEUSERAGENT_FALLBACK', None)
        self.ua = UserAgent(fallback=fallback)
        self.per_proxy = crawler.settings.get('RANDOM_UA_PER_PROXY', False)
        self.ua_type = crawler.settings.get('RANDOM_UA_TYPE', 'random')
        self.proxy2ua = {}

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        def get_ua():
            '''Gets random UA based on the type setting (random, firefox…)'''
            return getattr(self.ua, self.ua_type)
        
        if self.per_proxy:
            proxy = request.meta.get('proxy')
            if proxy not in self.proxy2ua:
                self.proxy2ua[proxy] = get_ua()
                logger.debug('Assign User-Agent %s to Proxy %s'
                             % (self.proxy2ua[proxy], proxy))
            request.headers.setdefault('User-Agent', self.proxy2ua[proxy])
        else:
            request.headers.setdefault('User-Agent', get_ua())
            
class RetryUserAgentMiddleware(RetryMiddleware):

    def __init__(self, settings):
        super(RetryUserAgentMiddleware, self).__init__(settings)

        fallback = settings.get('FAKEUSERAGENT_FALLBACK', None)
        self.ua = UserAgent(fallback=fallback)
        self.ua_type = settings.get('RANDOM_UA_TYPE', 'random')

    def get_ua(self):
        '''Gets random UA based on the type setting (random, firefox…)'''
        return getattr(self.ua, self.ua_type)

    def process_response(self, request, response, spider):
        if request.meta.get('dont_retry', False):
            return response
        if response.status in self.retry_http_codes:
            reason = response_status_message(response.status)
            request.headers['User-Agent'] = self.get_ua()
            return self._retry(request, reason, spider) or response
        return response
        
    def process_exception(self, request, exception, spider):
        if isinstance(exception, self.EXCEPTIONS_TO_RETRY) \
                and not request.meta.get('dont_retry', False):
            request.headers['User-Agent'] = self.get_ua()
            return self._retry(request, exception, spider)

