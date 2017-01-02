#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://bottles99oop.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='bottles',
    version='0.1.0',
    description='Metz and Owens OOP design course... but in python',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Laurence Billingham',
    author_email='laurence.billingham@gmail.com',
    url='https://github.com/lbillingham/bottles',
    packages=[
        'bottles',
    ],
    package_dir={'bottles': 'bottles'},
    include_package_data=True,
    install_requires=[
    ],
    license='MIT',
    zip_safe=False,
    keywords='bottles',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',  # want the f-strings
    ],
)
