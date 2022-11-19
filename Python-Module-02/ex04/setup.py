import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name = 'my_minipack',
      version = '1.0.0',
      author = 'clorin',
      author_email = 'clorin@student.42.fr',
      requires=[],
      license = 'GPL V3',
      packages = ['my_minipack'],
      description = 'Howto create a package in python',
      long_description = read('README.md'),
      platforms='Linux',
      url='',
      metadataversion='2.1',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Students',
        'Topic :: Education',
        'Topic :: HowTo',
        'Topic :: Packages',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only'
      ]
     )
