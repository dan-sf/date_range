import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(here, 'date_range', '__version__.py')) as fh:
    exec(fh.read(), about)

setup(
    name='date_range',
    description='Small command line utility used to print out consecutive dates',
    version = about['version'],
    packages=['date_range'],
    test_suite='tests',
    tests_require=[
        'mock',
    ],
    entry_points={ 'console_scripts': [ 'date_range = date_range.date_range:main', ] },
)

