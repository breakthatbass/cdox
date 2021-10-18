from setuptools import setup, find_packages
from cdox.__init__ import __version__, __author__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='cdox',
    version=f'{__version__}',
    description='automate documentation of c projects',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/breakthatbass/cdox',
    author=f'{__author__}',
    author_email='gamache.taylor@gmail.com',
    packages=find_packages(exclude=('tests',)),
    license='MIT',
    entry_points={
        'console_scripts' : ['cdox = cdox.__main__:main']
   }
)