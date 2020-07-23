import logging

from fake_useragent import UserAgent
from faker import Faker

logger = logging.getLogger(__name__)

class BaseProvider:
    '''
    Base class for providers. Doesn't provide much functionality for now,
    but it is a good placeholder for future additions
    '''
    def __init__(self, settings):
        self.settings = settings

        self._ua_type = None    # Each provider should set their own type of UA

    def get_random_ua(self):
        raise NotImplementedError


class FixedUserAgent(BaseProvider):
    '''
    Provided a fixed UA string, specified in Scrapy's settings.py
    '''
    def __init__(self, settings):
        super().__init__(settings)

        fixed_ua = settings.get('USER_AGENT', '')

        # If the USER_AGENT setting is not set, the useragent will be empty
        self._ua = fixed_ua or ''

    def get_random_ua(self):
        return self._ua


class FakeUserAgent(BaseProvider):
    '''
    Provides a random, real-life set of UA strings, powered by the fake_useragent library
    '''
    DEFAULT_UA_TYPE = 'random'
    def __init__(self, settings):
        super().__init__(settings)

        self._ua_type = settings.get('FAKE_USERAGENT_RANDOM_UA_TYPE', self.DEFAULT_UA_TYPE)

        fallback = settings.get('FAKEUSERAGENT_FALLBACK', None)
        self._ua = UserAgent(fallback=fallback)

    def get_random_ua(self):
        try:
            return getattr(self._ua, self._ua_type)()
        except AttributeError:
            logger.debug("Couldn't retrieve '%s' UA type. Using default: '%s'", self._ua_type, self.DEFAULT_UA_TYPE)


class Faker(BaseProvider):
    '''
    Provides a random set of UA strings, powered by the Faker library
    '''
    DEFAULT_UA_TYPE = 'user_agent'
    def __init__(self, settings):
        super().__init__(settings)

        self._ua = Faker()
        self._ua_type = settings.get('FAKER_RANDOM_UA_TYPE', self.DEFAULT_UA_TYPE)

    def get_random_ua(self):
        try:
            return getattr(self._ua, self._ua_type)()
        except AttributeError:
            logger.debug("Couldn't retrieve '%s' UA type. Using default: '%s'", self._ua_type, self.DEFAULT_UA_TYPE)
