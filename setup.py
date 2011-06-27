from distutils.core import setup
from setuptools import find_packages
from ponypusher import VERSION

setup(
#this is the name of the package to install from pypi/chishop
name='django-ponypusher',
description='Pusher app library for django',
author='Raymond McGinlay',
author_email='ray@lvlup.us',
#version number is derived from  VERSION attribute defined in __init.py__
version=VERSION,
#apps to be installed in package
packages=['ponypusher', ],
#python pusher library is required
install_requires=['pusher',],
license='GPL v3',
#Description that will appear on pypi/chishop
long_description=open('README.txt').read(),
include_package_data=True,
)
