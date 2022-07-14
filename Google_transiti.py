import sys
import os
import subprocess

# We must use setuptools, not distutils, because we need to use the
# namespace_packages option for the "google" package.
try:
  from setuptools import setup, Extension
except ImportError:
  sys.stderr.write(
    "Could not import setuptools; make sure you have setuptools or "
    "ez_setup installed.\n")
  raise

if __name__ == '__main__':
  ext_module_list = []

  setup(name = 'gtfs-realtime-bindings',
        version = '0.0.7',
        packages = ['google', 'google.transit'],
        namespace_packages = ['google'],
        install_requires = ['setuptools', 'protobuf'],
        url = 'https://github.com/MobilityData/gtfs-realtime-bindings',
        maintainer = 'MobilityData',
        maintainer_email = 'gtfs-realtime@googlegroups.com',
        license = 'Apache License, Version 2.0',
        description = 'Python classes generated from the GTFS-realtime protocol buffer specification.',
        classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules'
        ],
  )
