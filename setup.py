from setuptools import setup

setup(
    name='haris_first_package',
    version='1.0',
    description='A sample python package to learn how to maintain private python packages',
    author='Hari Krishnan',
    author_email='hariraghupathy@gmail.com',
    package_dir={
    'package_1': 'my_package_1',
    'package_2': 'my_package_2'
    },
    packages=['package_1', 'package_2']
)