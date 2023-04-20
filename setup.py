from setuptools import setup
from setuptools_scm.version import guess_next_version



setup(
    name='haris_first_package',
    version='1.0.1',
    description='A sample python package to learn how to maintain private python packages',
    author='Hari Krishnan',
    author_email='hariraghupathy@gmail.com',
    package_dir={
    'package_1': 'src/my_package_1',
    'package_2': 'src/my_package_2'
    },
    packages=['package_1', 'package_2'],
    include_package_data=True,
    zip_safe=False,
)


