from setuptools import find_packages, setup

setup(
    name='qwertystack_utils',
    packages=find_packages(include=['qwertystack_utils']),
    version='0.1.0',
    description='QwertyStack Python library with utilities',
    author='@QwertyStack',
    license='GNU General Public License v3.0',
    install_requires=['colorlog']
)