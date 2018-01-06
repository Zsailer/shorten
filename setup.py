#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'shorten'
DESCRIPTION = 'Easily shorten command line calls to alias'
URL = 'https://github.com/Zsailer/shorten'
EMAIL = 'zachsailer@gmail.com'
AUTHOR = 'Zach Sailer'

# Get homedir.
homedir = os.path.expanduser('~')

# Create .shorten folder in users home dir.
shorten_path = os.path.join(homedir, '.shorten')

# Check if shorten folder exists. Create if not.
if not os.path.exists(shorten_path):
    os.makedirs(shorten_path)

# Add shorten path to your bash_rc.
if os.path.exists(os.path.join(homedir, '.bash_rc')):
    rc_path = os.path.join(homedir, '.bash_rc')
elif os.path.exists(os.path.join(homedir, '.bashrc')):
    rc_path = os.path.join(homedir, '.bashrc')
elif os.path.exists(os.path.join(homedir, '.bash_profile')):
    rc_path = os.path.join(homedir, '.bash_profile')
else:
    rc_path = None

# Write shorten path to Bash RC if file exists.
if rc_path is not None:
    # Write to RC file.
    with open(rc_path, 'a') as f:
        f.write('export PATH="{}:$PATH"'.format(shorten_path))

# What packages are required for this module to be executed?
REQUIRED = []

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for
# that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.rst' is present in your MANIFEST.in file
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

# Load the package's __version__.py module as a dictionary.
about = {}
with open(os.path.join(here, NAME, '__version__.py')) as f:
    exec(f.read(), about)


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(
            sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        sys.exit()


# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    scripts=['scripts/shorten'],
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)
