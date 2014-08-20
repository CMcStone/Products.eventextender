from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='Products.eventextender',
      version=version,
      description="Adds additional fields to the plone ATEvent Type",
      long_description="",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone zope event',
      author='Carol McMasters-Stone',
      author_email='cbeck@Products.edu',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'archetypes.schemaextender',
          
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
