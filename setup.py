# -*- coding: utf-8 -*-
"""
This module contains the tool of gp.recipe.phantomjs
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    try:
        return open(os.path.join(os.path.dirname(__file__), *rnames)).read()
    except:
        return ''

version = '2.0.0.0'

long_description = (
    read('README.rst')
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read('CONTRIBUTORS.txt')
    + '\n' +
    'Change history\n'
    '**************\n'
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
   'Download\n'
    '********\n')

entry_point = 'gp.recipe.phantomjs:Recipe'
entry_points = {"zc.buildout": ["default = %s" % entry_point]}

tests_require = ['zope.testing', 'zc.buildout', 'Mock']

setup(name='gp.recipe.phantomjs',
      version=version,
      description="buildout recipe to install phantomjs/casperjs",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Buildout',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        ],
      keywords='buildout phantomjs casperjs',
      author='Gael Pasgrimaud',
      author_email='gael@gawel.org',
      url='http://github.com/gawel/gp.recipe.phantomjs',
      license='gpl',
      packages=find_packages(exclude=['ez_setup', 'tests',
                                      'bootstrap']),
      namespace_packages=['gp', 'gp.recipe'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'zc.buildout',
                        'zc.recipe.egg',
                        'hexagonit.recipe.download',
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='gp.recipe.phantomjs.tests',
      entry_points=entry_points,
      )
