from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='eurjel',
      version=version,
      description="EURJel code module",
      long_description="""\
""",
      classifiers=[], # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Jasper Op de Coul',
      author_email='jasper@infrae.com',
      url='',
      license='BSD',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      include_package_data=True,

      zip_safe=True,
      install_requires=[
    'nltk',
      ],
      )
