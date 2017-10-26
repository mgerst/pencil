#!/usr/bin/env python
from setuptools import setup, find_packages


setup(
    name='pencil',
    author='Matt Gerst',
    packages=find_packages(),
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest'
    ],
)
