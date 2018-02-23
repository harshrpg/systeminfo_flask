#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: Put package requirements here
]

setup_requirements = [
    # TODO(harshrpg): Put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: Put package test requirements here
]

setup(
    name='systeminfo_flask',
    version='0.1.0',
    description="This is flask application which can be run as a console script that will provide the information of the system it is installed in. It uses a private module systeminfo that can installed from https://guthub.com/harshrpg/systeminfo",
    long_description=readme + '\n\n' + history,
    author="Harsh Gupta",
    author_email='harsh.gupta@ucdconnect.ie',
    url='https://github.com/harshrpg/systeminfo_flask',
    packages=['app'],
    entry_points={
        'console_scripts': [
            'getPlatformInfo=app.run:main',
        ],
    },
    include_package_data=True,
    install_requires=['flask'],
    license="MIT license",
    zip_safe=False,
    keywords='systeminfo_flask',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
