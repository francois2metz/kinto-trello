from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='kinto-trello',
    version='0.1.2',

    description='Trello authentication plugin for Kinto',
    long_description=long_description,
    url='https://github.com/francois2metz/kinto-trello',
    author='François de Metz',
    author_email='francois@2metz.fr',
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='kinto trello',

    packages=find_packages(),

    install_requires=[],
)
