try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys

data = dict(
    name='python-datetime_tz',
    version='0.1',
    author='Tim Ansell',
    author_email='mithro@mithis.com',
    packages=['datetime_tz'],
    install_requires=['pytz', 'python-dateutil'],
)

setup(**data)
