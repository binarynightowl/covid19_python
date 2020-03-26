from setuptools import setup
import setuptools

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='covid19-data',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    description='A fast, powerful, and flexible way to get up to date COVID-19 data for any major city, state, '
                'country, and total world wide data',
    long_description=long_description,
    url='http://github.com/binarynightowl/covid19_python',
    author='Taylor Dettling',
    author_email='taylor@binarynightowl.com',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
