from setuptools import setup

setup(
    name='scrapy-fake-useragent',
    version='0.0.1',
    description='Use a random User-Agent provided by fake-useragent every request',
    long_description=open('README.md').read(),
    keywords='scrapy proxy',
    license='New BSD License',
    author="Alexander Afanasiev",
    author_email='afanasieffav@gmail.com',
    url='https://github.com/alecxe/scrapy-fake-useragent',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Scrapy'
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