#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import re
import sys

from setuptools import setup

name = 'drf-jsonmask'
package = 'drf_jsonmask'
description = "Implements Google\'s partial response in Django RestFramework (Fork from Zapier's package)"
url = 'https://github.com/jllorencetti/drf-jsonmask'
author = 'Craig Labenz, João Luiz Lorencetti (Fork author)'
author_email = "jll.linux@gmail.com"
license = 'BSD'


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]",
                     init_py, re.MULTILINE).group(1)


def get_long_description(package):
    """
    Read the contents of README.md
    """
    return open(os.path.join(package, '..', 'README.md')).read()


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


version = get_version(package)


if sys.argv[-1] == 'publish':
    if os.system("pip freeze | grep wheel"):
        print("wheel not installed.\nUse `pip install wheel`.\nExiting.")
        sys.exit()
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    print("You probably want to also tag the version now:")
    print("  git tag -a {0} -m 'version {0}'".format(version))
    print("  git push --tags")
    sys.exit()


setup(
    name=name,
    version=version,
    url=url,
    license=license,
    description=description,
    long_description=get_long_description(package),
    long_description_content_type='text/markdown',
    author=author,
    author_email=author_email,
    maintainer=author,
    maintainer_email=author_email,
    packages=get_packages(package),
    package_data=get_package_data(package),
    install_requires=[
        'jsonmask',
        'Django>=2.2,<4.1',
        'djangorestframework>=3.10,<3.14',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
