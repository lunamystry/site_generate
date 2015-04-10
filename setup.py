from setuptools import setup, find_packages

setup(
    name='gautengpug.github.io',
    version='0.2',
    description='Files for generating the Gauteng Python User Group static site',
    long_description = open('README.md', 'r').read() + open('AUTHORS.md', 'r').read(),
    author='gautengpug members',
    url='http://gautengpug.github.io',
    packages = find_packages(),
    install_requires = [
        'pelican',
        'fabric',
    ],
    zip_safe=False,
)

