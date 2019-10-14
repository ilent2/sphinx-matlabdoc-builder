# -*- coding: utf-8 -*-

# Based on sphinx-contrib/matlabdomain

from setuptools import setup, find_packages

with open('README.md', 'r') as f_readme:
    long_desc = f_readme.read()

version = '0.1.1'

requires = ['Sphinx>=1.7.2']

setup(
    name='sphinx-matlabdoc-builder',
    version=version,
    url='https://github.com/ilent2/sphinx-matlabdoc-builder',
    download_url='https://pypi.org/project/sphinx-matlabdoc-builder',
    license='BSD',
    author='Isaac Lenton',
    author_email='isaac@isuniversal.com',
    maintainer='Isaac Lenton',
    maintainer_email='isaac@isuniversal.com',
    description='A Sphinx extension for generating Matlab HTML docs.',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
        'Framework :: Sphinx :: Extension'
    ],
    keywords='sphinx docs documentation matlab',
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,


    entry_points = {
        'sphinx.builders': [
            'matlabdoc = sphinx_matlabdoc_builder',
        ],
    }
)
