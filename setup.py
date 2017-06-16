from setuptools import setup

setup(
    name='scrapy-fake-useragent',
    version='1.1.0',
    description='Use a random User-Agent provided by fake-useragent for every request',
    long_description=open('README.rst').read(),
    keywords='scrapy proxy user-agent web-scraping',
    license='New BSD License',
    author="Alexander Afanasyev",
    author_email='afanasieffav@gmail.com',
    url='https://github.com/alecxe/scrapy-fake-useragent',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Scrapy',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    packages=[
        'scrapy_fake_useragent',
    ],
    install_requires=[
        'fake-useragent'
    ],
)
