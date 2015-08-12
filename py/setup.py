#!/usr/bin/env python

from setuptools import setup, find_packages
import setuptools
from codecs import open
from os import path
import sparkling_water

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sparkling_water',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=sparkling_water.__version__,
    description='Sparkling Water integrates H2O\'s Fast Scalable Machine Learning with Spark',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/h2oai/sparkling-water.git',

    # Author details
    author='H2O.ai',
    author_email='support@0xdata.com',

    # Choose your license
    license='Apache v2',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='machine learning, data mining, statistical analysis, modeling, big data, distributed, parallel',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    # run-time dependencies
    install_requires=['requests', 'tabulate', 'h2o'],

    # include various data files using data_files
)
