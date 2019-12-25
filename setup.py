from setuptools import setup

setup(
    name='scrapy-fake-useragent',

    version='1.2.0',

    description='Use a random User-Agent provided by fake-useragent '
                'for every request',
    long_description=open('README.rst').read(),

    keywords='scrapy proxy user-agent web-scraping',
    license='New BSD License',

    author='Alexander Afanasyev',
    author_email='me@alecxe.me',
    maintainer='Alexander Afanasyev',
    maintainer_email='me@alecxe.me',

    url='https://github.com/alecxe/scrapy-fake-useragent',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Scrapy',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        'Topic :: Internet :: WWW/HTTP',
    ],
    packages=[
        'scrapy_fake_useragent',
    ],
    install_requires=[
        'fake-useragent'
    ],
)
