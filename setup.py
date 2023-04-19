from setuptools import setup

import versioneer

setup(
    name='haris_first_package',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='A sample python package to learn how to maintain private python packages',
    author='Hari Krishnan',
    author_email='hariraghupathy@gmail.com',
    package_dir={
    'package_1': 'src/my_package_1',
    'package_2': 'src/my_package_2'
    },
    packages=['package_1', 'package_2']
)