#!/usr/bin/env python3

from setuptools import setup
from setuptools import find_packages

setup(
    name='SolidProps',
    version='1.0',
    description='Library for calculating the thermodynamic properties of solids at temperatures from 1 to 300 K.',
    long_description=open('README.md').read(),
    author='Jakub Tkaczuk',
    author_email='jakub.tkaczuk@gmail.com',
    license='MIT',
    url='https://github.com/JakubTk/SolidProps',
    install_requires=[
        'pandas',
        'scipy',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.6',
)
