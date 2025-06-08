from setuptools import find_packages, setup

setup(
    name='aurup-desktop',
    version='0.1.0',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
)