""" setup.py """
import os
from setuptools import setup, find_packages
from pip.req import parse_requirements

def get_description():
    """ Makes README file into a string"""
    with open("README.rst") as file:
        long_description = file.read()
    return long_description

def get_reqs():
    """ Parses `requirements.txt` for dependencies"""
    parsed_reqs = parse_requirements("requirements/common.txt", session=False)
    reqs = [str(ir.req) for ir in parsed_reqs]
    return reqs

def get_version():
    """ Gets version from impyute.__init__.py

    Runs `impyute.__init__` and loads defined variables into scope
    """
    with open(os.path.join('impyute', '__init__.py')) as version_file:
        # pylint: disable=exec-used, undefined-variable
        exec(version_file.read(), globals())
        return __version__


setup(
    name='dieharder',
    author='Elton Law',
    author_email='eltonlaw296@gmail.com',
    version=get_version(),
    url="http://dieharder.readthedocs.io/en/latest/",
    download_url='https://github.com/eltonlaw/dieharder',
    description='Tests for randomness.',
    long_description=get_description(),
    packages=find_packages(exclude=['docs']),
    install_requires=get_reqs(),
    keywords=["rng", "tests"],
    classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Science/Research',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python',
                 'Topic :: Software Development',
                 'Topic :: Scientific/Engineering'],
    extras_require={
        'dev': ['pylint', 'sphinx'],
        'test': ['pytest'],
    },
    license='GPL-3.0'
)
