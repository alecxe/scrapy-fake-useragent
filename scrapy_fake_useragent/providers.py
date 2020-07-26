import logging
from abc import abstractmethod

import fake_useragent
from faker import Faker

logger = logging.getLogger(__name__)


class BaseProvider:
    """
    Base class for providers.
    Doesn't provide much functionality for now,
    but it is a good placeholder for future additions.
    """

    def __init__(self, settings):
        self.settings = settings

        # Each provider should set their own type of UA
        self._ua_type = None

    @abstractmethod
    def get_random_ua(self):
        """
        Method needs to be implemented per provider based on BaseProvider.
        """


class FixedUserAgentProvider(BaseProvider):
    """Provides a fixed UA string, specified in Scrapy's settings.py"""

    def __init__(self, settings):
        BaseProvider.__init__(self, settings)

        fixed_ua = settings.get('USER_AGENT', '')

        # If the USER_AGENT setting is not set, the useragent will be empty
        self._ua = fixed_ua or ''

    def get_random_ua(self):
        return self._ua


class FakeUserAgentProvider(BaseProvider):
    """
    Provides a random, real-world set of UA strings,
    powered by the fake_useragent library.
    """

    DEFAULT_UA_TYPE = 'random'

    def __init__(self, settings):
        BaseProvider.__init__(self, settings)

        self._ua_type = settings.get('FAKE_USERAGENT_RANDOM_UA_TYPE',
                                     self.DEFAULT_UA_TYPE)

        fallback = settings.get('FAKEUSERAGENT_FALLBACK', None)
        self._ua = fake_useragent.UserAgent(fallback=fallback)

    def get_random_ua(self):
        """
        If the UA type attribute is not found,
        fake user agent provider falls back to fallback by default.
        No need to handle AttributeError.
        """
        return getattr(self._ua, self._ua_type)


class FakerProvider(BaseProvider):
    """
    Provides a random set of UA strings, powered by the Faker library.
    """

    DEFAULT_UA_TYPE = 'user_agent'

    def __init__(self, settings):
        BaseProvider.__init__(self, settings)

        self._ua = Faker()
        self._ua_type = settings.get('FAKER_RANDOM_UA_TYPE',
                                     self.DEFAULT_UA_TYPE)

    def get_random_ua(self):
        try:
            return getattr(self._ua, self._ua_type)()
        except AttributeError:
            logger.debug("Couldn't retrieve '%s' UA type. "
                         "Using default: '%s'",
                         self._ua_type, self.DEFAULT_UA_TYPE)
            return getattr(self._ua, self.DEFAULT_UA_TYPE)()
